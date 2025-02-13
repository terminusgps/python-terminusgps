import threading
import logging
import typing
import dataclasses
import datetime

from wialon.api import WialonError
from wialon.api import Wialon as WialonAPI
from django.conf import settings
from django.utils import timezone

from terminusgps.wialon.errors import WialonLogoutError, WialonLoginError


@dataclasses.dataclass
class WialonAPICall:
    action: str
    timestamp: datetime.datetime
    args: tuple
    kwargs: dict
    result: typing.Any = None
    error: Exception | None = None


class Wialon(WialonAPI):
    def __init__(self, log_level: int = logging.INFO, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.call_history: list[WialonAPICall] = []
        self.logger = self.create_logger(log_level)

    @property
    def total_calls(self) -> int:
        return len(self.call_history)

    @property
    def successful_calls(self) -> list[WialonAPICall | None]:
        return [call for call in self.call_history if not call.error]

    @property
    def failed_calls(self) -> list[WialonAPICall | None]:
        return [call for call in self.call_history if call.error]

    @property
    def failure_rate(self) -> float:
        return len(self.failed_calls) / self.total_calls

    def call(self, action_name: str, *argc, **kwargs) -> typing.Any:
        self.logger.info(f"Executing '{action_name}'...")
        self.logger.debug(f"Executing '{action_name}' using: '{kwargs}'")
        call_record = WialonAPICall(
            action=action_name, timestamp=timezone.now(), args=argc, kwargs=kwargs
        )

        try:
            result = super().call(action_name, *argc, **kwargs)
            call_record.result = result
            return result
        except WialonError as e:
            self.logger.warning(f"Failed to execute '{action_name}': '{e}'")
            call_record.error = e
            raise
        finally:
            self.call_history.append(call_record)

    def create_logger(self, log_level: int) -> logging.Logger:
        logger = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        logger.setLevel(log_level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger


class WialonSession:
    def __init__(
        self,
        token: str | None = None,
        sid: str | None = None,
        uid: str | None = None,
        scheme: str = "https",
        host: str = "hst-api.wialon.com",
        port: int = 443,
        log_level: int = logging.INFO,
    ) -> None:
        """
        Starts or continues a Wialon API session.

        :param token: An optional Wialon API token. Default is :confval:`WIALON_TOKEN`.
        :type token: :py:obj:`str` | :py:obj:`None`
        :param sid: An optional Wialon API session id. If provided, the session is continued.
        :type sid: :py:obj:`str` | :py:obj:`None`
        :raises ImproperlyConfigured: If either :confval:`WIALON_TOKEN` or :confval:`WIALON_ADMIN_ID` is not set.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """

        self.wialon_api = Wialon(
            scheme=scheme, host=host, port=port, sid=sid, log_level=log_level
        )
        self.token = token
        self.login_id = uid
        self._username = None
        self._gis_sid = None
        self._hw_gp_ip = None
        self._wsdk_version = None
        self._uid = None
        self.logger = self.create_logger(log_level)

    def create_logger(self, log_level: int) -> logging.Logger:
        logger = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        logger.setLevel(log_level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def __enter__(self) -> "WialonSession":
        assert self.token, "Wialon API token was not set"
        self.login(self.token)
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.logout()

    @property
    def gis_geocode(self) -> str | None:
        """
        Gis geocode URL.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._gis_geocode

    @property
    def gis_render(self) -> str | None:
        """
        Gis rendering URL.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._gis_render

    @property
    def gis_routing(self) -> str | None:
        """
        Gis routing URL.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._gis_routing

    @property
    def gis_search(self) -> str | None:
        """
        Gis search URL.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._gis_search

    @property
    def gis_sid(self) -> str | None:
        """
        Gis session id.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._gis_sid

    @property
    def host(self) -> str | None:
        """
        IP of the client hosting the Wialon session.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._host

    @property
    def hw_gw_ip(self) -> str | None:
        """
        Hardware gateway IP.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._hw_gw_ip

    @property
    def hw_gw_dns(self) -> str | None:
        """
        Hardware gateway domain name, should evaluate to :py:attr:`hw_gw_ip` if present.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._hw_gw_dns

    @property
    def wsdk_version(self) -> str | None:
        """
        The Wialon Source Developer Kit (WSDK) version number of the session.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._wsdk_version

    @property
    def uid(self) -> str | None:
        """
        A Wialon user ID this session is operating as.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`
        """
        return self._uid

    @property
    def username(self) -> str | None:
        """
        A Wialon username the session is operating as.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self._username

    @property
    def id(self) -> str | None:
        """
        Shortcut property for :py:attr:`WialonSession.wialon_api.sid`.

        Returns :py:obj:`None` if the session wasn't logged in.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

        """
        return self.wialon_api.sid

    @property
    def token(self) -> str:
        """
        A Wialon API token set during :py:meth:`WialonSession.__init__`.

        Default token value is :confval:`WIALON_TOKEN`.

        :type: :py:obj:`str`
        :value: :confval:`WIALON_TOKEN`

        """
        return self._token

    @token.setter
    def token(self, value: str | None = None) -> None:
        self._token = value if value else settings.WIALON_TOKEN

    def login(self, token: str, flags: int = sum([0x1, 0x2, 0x20])) -> str:
        """
        Logs into the Wialon API and starts a new session.

        :param token: An active Wialon API token.
        :type token: :py:obj:`str`
        :param flags: A login response flag integer.
        :type flags: :py:obj:`int`
        :raises WialonLoginError: If the login fails.
        :returns: The new session id.
        :rtype: :py:obj:`str`

        """
        try:
            response = self.wialon_api.token_login(**{"token": token, "fl": flags})
            self._set_login_response(response)
            self.logger.info(f"Logged into Wialon API session '{response.get('eid')}'")
            return response.get("eid")
        except (WialonError, AssertionError) as e:
            self.logger.critical(f"Failed to login to Wialon API: '{e}'")
            raise WialonLoginError(token, e)

    def logout(self) -> None:
        """
        Logs out of the Wialon API session.

        :raises WialonLogoutError: If the logout fails.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        response: dict = self.wialon_api.core_logout({})
        self.logger.info(
            f"Logged out of session '{self.id}' after {self.wialon_api.total_calls} Wialon API calls."
        )
        self.logger.debug(f"Failure rate: {self.wialon_api.failure_rate}%")
        if response.get("error") != 0:
            self.logger.warning(
                f"Failed to logout of session: '{response.get('message')}'"
            )
            raise WialonLogoutError(str(self.id))

    def _set_login_response(self, login_response: dict) -> None:
        """
        Sets the Wialon API session's attributes based on a login response.

        :param login_response: A response returned from :py:meth:`login` or :py:meth:`duplicate`.
        :type login_response: :py:obj:`dict`
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        self.wialon_api.sid = login_response.get("eid")
        self._gis_geocode = login_response.get("gis_geocode")
        self._gis_render = login_response.get("gis_render")
        self._gis_routing = login_response.get("gis_routing")
        self._gis_search = login_response.get("gis_search")
        self._gis_sid = login_response.get("gis_sid")
        self._host = login_response.get("host")
        self._hw_gw_dns = login_response.get("hw_gw_dns")
        self._hw_gw_ip = login_response.get("hw_gw_ip")
        self._uid = login_response.get("user", {}).get("id")
        self._nm = login_response.get("user", {}).get("nm")
        self._username = login_response.get("au")
        self._video_service_url = login_response.get("video_service_url")
        self._wsdk_version = login_response.get("wsdk_version")


class WialonSessionManager:
    _instance = None
    _lock = threading.Lock()
    _session = None

    def __new__(cls) -> "WialonSessionManager":
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance

    def get_session(
        self, sid: str | None = None, log_level: int = logging.INFO
    ) -> WialonSession:
        with self._lock:
            if not self._session:
                self._session = WialonSession(sid=sid, log_level=log_level)
        return self._session
