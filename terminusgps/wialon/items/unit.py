import logging
from urllib.parse import quote_plus

from terminusgps.wialon import flags
from terminusgps.wialon.items.base import WialonBase


class WialonUnit(WialonBase):
    def create(self, **kwargs) -> int | None:
        """
        Creates a new Wialon unit.

        :param creator_id: A Wialon user id.
        :type creator_id: :py:obj:`int`
        :param name: A new name for the unit.
        :type name: :py:obj:`str`
        :param hw_type_id: A Wialon hardware type ID.
        :type hw_type_id: :py:obj:`str`
        :returns: The Wialon id for the new unit.
        :rtype: :py:obj:`int` | :py:obj:`None`

        """
        if not kwargs.get("creator_id"):
            raise ValueError("'creator_id' is required on creation.")
        if not kwargs.get("name"):
            raise ValueError("'name' is required on creation.")
        if not kwargs.get("hw_type_id"):
            raise ValueError("'hw_type_id' is required on creation.")

        response = self.session.wialon_api.core_create_unit(
            **{
                "creatorId": kwargs["creator_id"],
                "name": kwargs["name"],
                "hwTypeId": kwargs["hw_type_id"],
                "dataFlags": flags.DATAFLAG_UNIT_BASE,
            }
        )
        return response.get("item", {}).get("id")

    @property
    def available_commands(self) -> dict:
        return self.session.wialon_api.core_get_hw_cmds(
            **{"deviceTypeId": 0, "unitId": self.id}
        )

    def execute_command(
        self,
        name: str,
        link_type: str,
        timeout: int = 5,
        flags: int = 0,
        param: dict | None = None,
    ) -> None:
        """
        Executes a command on this Wialon unit.

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
        Sets a new access password for this Wialon unit.

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
        Activates this Wialon unit.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """

        self.session.wialon_api.unit_set_active(
            **{"itemId": self.id, "active": int(True)}
        )

    def deactivate(self) -> None:
        """
        Deactivates this Wialon unit.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """

        self.session.wialon_api.unit_set_active(
            **{"itemId": self.id, "active": int(False)}
        )

    def assign_phone(self, phone: str) -> None:
        """
        Assigns a phone number to this Wialon unit.

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

        This includes any attached drivers, custom/admin fields, or otherwise assigned phone numbers.

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
        cleaned_phones = []
        for num in phones:
            if "," in num:
                cleaned_phones.extend(num.split(","))
            else:
                cleaned_phones.append(num)
        return cleaned_phones

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
            dirty_phones = [driver[0].get("ph") for _, driver in response.items()]
            return self.clean_phone_numbers(dirty_phones)
