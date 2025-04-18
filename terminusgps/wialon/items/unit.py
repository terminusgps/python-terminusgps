from urllib.parse import quote_plus, urljoin

from django.conf import settings

from terminusgps.wialon import flags
from terminusgps.wialon.items.base import WialonBase


class WialonUnit(WialonBase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._imei_number = None
        self._active = None
        self._image_uri = None

    def create(
        self, creator_id: str | int, name: str, hw_type_id: str | int
    ) -> int | None:
        """
        Creates a new Wialon unit.

        :param creator_id: A Wialon user id.
        :type creator_id: :py:obj:`str` | :py:obj:`int`
        :param name: A name for the unit.
        :type name: :py:obj:`str`
        :param hw_type_id: A Wialon hardware type ID.
        :type hw_type_id: :py:obj:`str` | :py:obj:`int`
        :raises ValueError: If ``creator_id`` is a :py:obj:`str` but not a digit.
        :raises ValueError: If ``hw_type_id`` is a :py:obj:`str` but not a digit.
        :returns: An id for the new unit.
        :rtype: :py:obj:`int` | :py:obj:`None`

        """
        if isinstance(creator_id, str) and not creator_id.isdigit():
            raise ValueError(f"'creator_id' must be a digit, got '{creator_id}'.")
        if isinstance(hw_type_id, str) and not hw_type_id.isdigit():
            raise ValueError(f"'hw_type_id' must be a digit, got '{hw_type_id}'.")

        response = self.session.wialon_api.core_create_unit(
            **{
                "creatorId": creator_id,
                "name": name,
                "hwTypeId": hw_type_id,
                "dataFlags": flags.DataFlag.UNIT_BASE,
            }
        )
        return (
            int(response.get("item", {}).get("id"))
            if response and response.get("item")
            else None
        )

    def populate(self) -> None:
        super().populate()
        response = self.session.wialon_api.core_search_item(
            **{
                "id": self.id,
                "flags": (
                    flags.DataFlag.UNIT_ADVANCED_PROPERTIES
                    | flags.DataFlag.UNIT_IMAGE
                    | flags.DataFlag.UNIT_ADMIN_FIELDS
                ).value,
            }
        )
        if response is not None:
            item = response.get("item", {})
            self._imei_number = item.get("uid")
            self._active = item.get("act", False)
            self._image_uri = item.get("uri")

    def get_position(self) -> dict | None:
        return self.session.wialon_api.core_search_item(
            **{"id": self.id, "flags": flags.DataFlag.UNIT_POSITION.value}
        )

    @property
    def position(self) -> dict | None:
        """Current GPS position of the unit."""
        return self.get_position()

    @property
    def exists(self) -> bool:
        """Whether or not the unit exists in Wialon."""
        return bool(
            self.session.wialon_api.core_search_item(
                **{"id": self.id, "flags": flags.DataFlag.UNIT_BASE.value}
            ).get("item", False)
        )

    @property
    def available_commands(self) -> dict:
        """
        Commands assigned to the unit.

        :type: :py:obj:`dict`

        """
        return self.session.wialon_api.core_get_hw_cmds(
            **{"deviceTypeId": 0, "unitId": self.id}
        )

    @property
    def image_uri(self) -> str:
        """
        Image URI for the unit.

        :type :py:obj:`str`

        """
        if self._image_uri is None:
            self.populate()
        return str(self._image_uri)

    @property
    def imei_number(self) -> str:
        """
        IMEI # for the unit.

        :type: :py:obj:`str`

        """
        if self._imei_number is None:
            self.populate()
        return str(self._imei_number)

    @property
    def iccid(self) -> str | None:
        """
        SIM Card # for the unit, if any.

        :type: :py:obj:`str` | :py:obj:`None`

        """
        return self.afields.get("iccid")

    @property
    def carrier(self) -> str | None:
        """
        Name of the telecommunications company associated with the unit's SIM card, if any.

        :type: :py:obj:`str` | :py:obj:`None`

        """
        return self.afields.get("carrier")

    @property
    def active(self) -> bool:
        """Whether or not the unit is activated."""
        if self._active is None:
            self.populate()
        return bool(self._active)

    @property
    def image_url(self) -> str | None:
        if hasattr(settings, "WIALON_HOST"):
            return urljoin(settings.WIALON_HOST, self._image_uri)
        return urljoin("https://hst-api.wialon.com", self._image_uri)

    def execute_command(
        self,
        name: str,
        link_type: str,
        timeout: int = 5,
        flags: int = 0,
        param: dict | None = None,
    ) -> None:
        """
        Executes a command on the unit.

        :param name: A Wialon command name.
        :type name: :py:obj:`str`
        :param link_type: A protocol to use for the Wialon command.
        :type link_type: :py:obj:`str`
        :param timeout: How long (in seconds) to wait before timing out command execution. Default is ``5``.
        :type timeout: :py:obj:`int`
        :param flags: Flags to pass to the Wialon command execution.
        :type flags: :py:obj:`int`
        :param param: Additional parameters to execute the command with.
        :type param: :py:obj:`dict` | :py:obj:`None`
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        self.session.wialon_api.unit_exec_cmd(
            **{
                "itemId": self.id,
                "commandName": name,
                "linkType": link_type,
                "timeout": timeout,
                "flags": flags,
                "param": param if param else {},
            }
        )

    def set_access_password(self, password: str) -> None:
        """
        Sets a new access password for the unit.

        :param password: A new access password.
        :type name: :py:obj:`str`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        self.session.wialon_api.unit_update_access_password(
            **{"itemId": self.id, "accessPassword": password}
        )

    def activate(self) -> None:
        """
        Activates the unit.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        self.session.wialon_api.unit_set_active(
            **{"itemId": self.id, "active": int(True)}
        )

    def deactivate(self) -> None:
        """
        Deactivates the unit.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        self.session.wialon_api.unit_set_active(
            **{"itemId": self.id, "active": int(False)}
        )

    def assign_phone(self, phone: str) -> None:
        """
        Assigns a phone number to the unit.

        :param phone: A phone number beginning with a country code.
        :type phone: :py:obj:`str`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        self.session.wialon_api.unit_update_phone(
            **{"itemId": self.id, "phoneNumber": quote_plus(phone)}
        )

    def get_phone_numbers(self) -> list[str]:
        """
        Retrieves all phone numbers assigned to the unit.

        This includes any attached drivers, custom/admin fields or otherwise assigned phone numbers.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: A list of phone numbers.
        :rtype: :py:obj:`list`

        """
        phone_numbers: list[str] = []
        phones_0: list[str] | None = self._get_driver_phone_numbers()
        phones_1: list[str] | None = self._get_cfield_phone_numbers()
        phones_2: list[str] | None = self._get_afield_phone_numbers()

        if phones_0 is not None:
            phone_numbers.extend(phones_0)
        if phones_1 is not None:
            phone_numbers.extend(phones_1)
        if phones_2 is not None:
            phone_numbers.extend(phones_2)
        return list(dict.fromkeys(phone_numbers))  # Removes duplicate phone numbers

    def clean_phone_numbers(self, phones: list[str]) -> list[str]:
        """Takes a list of phone numbers and returns a list of clean phone numbers."""
        return [
            clean_num
            for num in phones
            for clean_num in (num.split(",") if "," in num else [num])
        ]

    def _get_afield_phone_numbers(self, key: str = "to_number") -> list[str] | None:
        """
        Retrives any phone numbers saved in an admin field by key.

        :param key: An admin field key. Default is ``"to_number"``.
        :type key: :py:obj:`str`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: A list of phone numbers, if the unit has admin phone number fields.
        :rtype: :py:obj:`list` | :py:obj:`None`

        """
        for field_name, field_val in self.afields.items():
            if field_name == key:
                return self.clean_phone_numbers([field_val])

    def _get_cfield_phone_numbers(self, key: str = "to_number") -> list[str] | None:
        """
        Retrives any phone numbers saved in a custom field by key.

        :param key: A custom field key. Default is ``"to_number"``.
        :type key: :py:obj:`str`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: A list of phone numbers, if the unit has custom phone number fields.
        :rtype: :py:obj:`list` | :py:obj:`None`

        """
        for field_name, field_val in self.cfields.items():
            if field_name == key:
                return self.clean_phone_numbers([field_val])

    def _get_driver_phone_numbers(self) -> list[str] | None:
        """
        Retrieves any phone numbers assigned to drivers attached to the unit.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: A list of phone numbers, if the unit has attached drivers with phone numbers.
        :rtype: :py:obj:`list` | :py:obj:`None`

        """
        response = self.session.wialon_api.resource_get_unit_drivers(
            **{"unitId": self.id}
        )
        if response:
            dirty_phones = [driver[0].get("ph") for driver in response.values()]
            return self.clean_phone_numbers(dirty_phones)
