from dataclasses import dataclass
from wialon.api import Wialon, WialonError
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .errors import WialonLogoutError, WialonLoginError


@dataclass
class WialonLoginResponseUser:
    nm: str
    cls: str
    id: str
    prp: dict | None
    crt: str | None
    bact: str | None


@dataclass
class WialonLoginResponse:
    sid: str
    gis_sid: str
    host: str
    hw_gw_ip: str
    au: str
    pi: str
    tm: str
    wsdk_version: str
    user: None | WialonLoginResponseUser


class WialonSessionBase:
    def __init__(self, token: str | None = None, sid: str | None = None) -> None:
        if not hasattr(settings, "WIALON_TOKEN"):
            raise ImproperlyConfigured("'WIALON_TOKEN' setting is required.")
        self.token = token
        self.wialon_api = Wialon(
            scheme="https", host="hst-api.wialon.com", port=443, sid=sid
        )

    @property
    def id(self) -> str | None:
        return self.wialon_api.sid

    @property
    def token(self) -> str | None:
        return self._token

    @token.setter
    def token(self, value: str | None = None) -> None:
        self._token = value if value else settings.WIALON_TOKEN

    def login(self, token: str | None = None, flags: int | None = None) -> None:
        """Logs into the Wialon API and starts a new session."""
        if not token:
            raise ValueError("Must provide a Wialon API token to login with.")
        if not flags:
            flags = sum([0x1, 0x2, 0x20])

        try:
            response = self.wialon_api.token_login(
                **{"token": token, "fl": sum([0x1, 0x2, 0x20])}
            )
            self._set_login_response(WialonLoginResponse(**response))

        except WialonError as e:
            raise WialonLoginError(token, e)

    def logout(self) -> None:
        """Logs out of the Wialon API and raises an error if the session was not destroyed."""
        sid: str = str(self.id)
        logout_response = self.wialon_api.core_logout({})
        if logout_response.get("error") != 0:
            raise WialonLogoutError(sid)

    def _set_login_response(self, login_response: WialonLoginResponse) -> None:
        self.wialon_api.sid = login_response.sid
        self.username = login_response.au
        self.gis_sid = login_response.gis_sid
        self.host = login_response.host
        self.hw_gp_ip = login_response.hw_gw_ip
        self.wsdk_version = login_response.wsdk_version
        self.uid = login_response.user.id if login_response.user else None


class WialonSession(WialonSessionBase):
    def __enter__(self) -> "WialonSession":
        assert self.token is not None
        self.login(self.token)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        self.logout()
        return
