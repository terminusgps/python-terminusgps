from urllib.parse import quote_plus

from terminusgps.wialon import flags
from terminusgps.wialon.items.base import WialonBase


class WialonResource(WialonBase):
    def create(
        self, creator_id: str | int, name: str, skip_creator_check: bool = False
    ) -> int | None:
        """
        Creates a new Wialon resource.

        :param creator_id: A Wialon user id.
        :type creator_id: :py:obj:`int` | :py:obj:`str`
        :param name: A name for the resource.
        :type name: :py:obj:`str`
        :param skip_creator_check: Bypass object creation restrictions while creating the resource.
        :type skip_creator_check: :py:obj:`bool`
        :raises ValueError: If ``creator_id`` is not a digit.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: The Wialon id for the new resource, if it was created.
        :rtype: :py:obj:`int` | :py:obj:`None`

        """
        if isinstance(creator_id, str) and not creator_id.isdigit():
            raise ValueError(f"'creator_id' must be a digit, got '{creator_id}'.")

        response = self.session.wialon_api.core_create_resource(
            **{
                "creatorId": creator_id,
                "name": name,
                "dataFlags": flags.DATAFLAG_UNIT_BASE,
                "skipCreatorCheck": int(skip_creator_check),
            }
        )
        return int(response.get("item", {}).get("id")) if response.get("item") else None

    def delete(self) -> None:
        """
        Deletes all micro-objects assigned to the resource.

        If the resource is an account, instead deletes all macro-objects and micro-objects assigned to the account.

        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        self.delete_account() if self.is_account else super().delete()

    @property
    def is_dealer(self) -> bool:
        """
        Whether or not the resource/account has dealer rights.

        If the resource is **not** an account, this always returns :py:obj:`False`.

        :type: :py:obj:`bool`

        """
        if not self.is_account:
            return False  # Resources cannot have dealer rights
        return bool(
            self.session.wialon_api.get_account_data(
                **{"itemId": self.id, "type": 1}
            ).get("dealerRights")
        )

    @property
    def is_account(self) -> bool:
        """
        Whether or not the resource is an account.

        :type: :py:obj:`bool`

        """
        response = self.session.wialon_api.core_search_item(
            **{"id": self.id, "flags": flags.DATAFLAG_RESOURCE_BILLING_PROPERTIES}
        )
        return int(response.get("item", {}).get("bact")) == self.id

    def is_migrated(self, unit: WialonBase) -> bool:
        """
        Checks if a unit is migrated into the account.

        :param unit: A Wialon object.
        :type unit: :py:obj:`~terminusgps.wialon.items.base.WialonBase`
        :returns: Whether or not the unit is migrated into the account.
        :rtype: :py:obj:`bool`

        """
        assert self.is_account, "The resource is not an acccount"
        response = self.session.wialon_api.account_list_change_accounts(
            **{"units": [unit.id]}
        )
        results = [self.id == int(item.get("id")) for item in response]
        return any(results)

    def set_dealer_rights(self, enabled: bool = False) -> None:
        """
        Sets dealer rights on the account.

        You **probably don't** need to use this method.

        :param enabled: :py:obj:`True` to enable dealer rights, :py:obj:`False` to disable dealer rights. Default is :py:obj:`False`.
        :type enabled: :py:obj:`bool`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert self.is_account, "The resource is not an account"
        self.session.wialon_api.account_update_dealer_rights(
            **{"itemId": self.id, "enable": str(enabled).lower()}
        )

    def migrate_unit(self, unit: WialonBase) -> None:
        """
        Migrates a :py:obj:`WialonUnit` into the account.

        :param unit: A Wialon object.
        :type unit: :py:obj:`~terminusgps.wialon.items.base.WialonBase`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert self.is_account, "The resource is not an account"
        self.session.wialon_api.account_change_account(
            **{"itemId": unit.id, "resourceId": self.id}
        )

    def update_plan(self, new_plan: str) -> None:
        """
        Updates the account billing plan.

        :param new_plan: The name of a billing plan.
        :type new_plan: :py:obj:`str`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert self.is_account, "The resource is not an account"
        self.session.wialon_api.account_update_plan(
            **{"itemId": self.id, "plan": new_plan}
        )

    def create_account(self, billing_plan: str) -> None:
        """
        Transforms the resource into an account.

        :param billing_plan: The name of a billing plan.
        :type billing_plan: :py:obj:`str`
        :raises AssertionError: If the resource is already account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert not self.is_account, "The resource is already an account"
        self.session.wialon_api.account_create_account(
            **{"itemId": self.id, "plan": billing_plan}
        )
        self.set_settings_flags()

    def delete_account(self) -> None:
        """
        Deletes the account if it exists, as well as any micro-objects and macro-objects it contains.

        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert self.is_account, "The resource is not an account"
        self.session.wialon_api.account_delete_account(**{"itemId": self.id})

    def enable_account(self) -> None:
        """
        Enables the Wialon account.

        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert self.is_account, "The resource is not an account"
        self.session.wialon_api.account_enable_account(
            **{"itemId": self.id, "enable": int(True)}
        )

    def disable_account(self) -> None:
        """
        Disables the Wialon account.

        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert self.is_account, "The resource is not an account"
        self.session.wialon_api.account_enable_account(
            **{"itemId": self.id, "enable": int(False)}
        )

    def set_minimum_days(self, days: int = 0) -> None:
        """
        Sets the minimum days counter value to ``days``.

        :param days: Number of days to set the counter to. Default is ``0``.
        :type days: :py:obj:`int`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert self.is_account, "The resource is not an account"
        self.session.wialon_api.account_update_min_days(
            **{"itemId": self.id, "minDays": days}
        )

    def add_days(self, days: int = 30) -> None:
        """
        Adds days to the account.

        :param days: Number of days to add to the account. Default is ``30``.
        :type days: :py:obj:`int`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert self.is_account, "The resource is not an account"
        self.session.wialon_api.account_do_payment(
            **{
                "itemId": self.id,
                "balanceUpdate": "0.00",
                "daysUpdate": days,
                "description": f"{self.session.id} - Added {days} days.",
            }
        )

    def set_settings_flags(
        self,
        flags: int = 0x20,
        block_balance_val: float = 0.00,
        deny_balance_val: float = 0.00,
    ) -> None:
        """
        Sets account settings flags.

        :param flags: A flag integer to set on the account.
        :type flags: :py:obj:`int`
        :param block_balance_val: Minimum amount on the account's balance before blocking the account.
        :type block_balance_val: :py:obj:`float`
        :param deny_balance_val: Minimum amount on the account's balance before denying the account.
        :type deny_balance_val: :py:obj:`float`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        assert self.is_account, "The resource is not an account"
        self.session.wialon_api.account_update_flags(
            **{
                "itemId": self.id,
                "flags": flags,
                "blockBalance": block_balance_val,
                "denyBalance": deny_balance_val,
            }
        )

    def create_driver(
        self,
        name: str,
        code: str = "",
        desc: str = "",
        phone: str = "",
        mobile_auth_code: str = "",
        custom_fields: dict[str, str] | None = None,
    ) -> None:
        """
        Creates a driver for the resource.

        :param name: A name for the new driver.
        :type name: :py:obj:`str`
        :param code: A unique code for the new driver.
        :type code: :py:obj:`str`
        :param desc: Description for the driver.
        :type desc: :py:obj:`str`
        :param phone: A phone number beginning in a country code. No spaces.
        :type phone: :py:obj:`str`
        :param mobile_auth_code: Authentication code for Wialon mobile app.
        :type mobile_auth_code: :py:obj:`str`
        :param image_checksum: Checksum for driver image.
        :type image_checksum: :py:obj:`str`
        :param image_ratio: Driver image aspect ratio.
        :type image_ratio: :py:obj:`float` | :py:obj:`None`
        :param custom_fields: Additional custom fields to add to the driver.
        :type custom_fields: :py:obj:`dict` | :py:obj:`None`
        :raises WialonError: If something goes wrong calling the Wialon API.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        params = {
            "itemId": self.id,
            "id": 0,
            "callMode": "create",
            "ej": {"apps": []},
            "c": code,
            "ds": desc,
            "n": name,
            "f": 1,
            "pwd": mobile_auth_code,
        }

        if phone:
            params.update({"p": quote_plus(phone)})
        if custom_fields:
            params.update({"jp": custom_fields})
        self.session.wialon_api.resource_update_driver(**params)

    def create_passenger(
        self,
        name: str,
        code: str,
        phone: str = "",
        custom_fields: dict[str, str] | None = None,
    ) -> None:
        """
        Creates a passenger/tag for the resource.

        :param name: A name for the new passenger.
        :type name: :py:obj:`str`
        :param code: A unique code for the new passenger.
        :type code: :py:obj:`str`
        :param phone: A phone number beginning in a country code. No spaces.
        :type phone: :py:obj:`str`
        :param custom_fields: Additional custom fields to add to the passenger.
        :type custom_fields: :py:obj:`dict` | :py:obj:`None`
        :raises WialonError: If something goes wrong calling the Wialon API.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        params = {
            "itemId": self.id,
            "id": 0,
            "callMode": "create",
            "c": code,
            "n": name,
        }
        if phone:
            params.update({"p": quote_plus(phone)})
        if custom_fields:
            params.update({"jp": custom_fields})
        self.session.wialon_api.resource_update_tag(**params)

    def update_attachable_drivers(self, units: list[str | int]) -> None:
        """Updates the pool of units for the resource to attach drivers to the new unit list."""
        self.session.wialon_api.update_driver_units(
            **{"itemId": self.id, "units": units}
        )

    def update_attachable_passengers(self, units: list[str | int]) -> None:
        """Updates the pool of units for the resource to attach passengers to the new unit list."""
        self.session.wialon_api.update_tag_units(**{"itemId": self.id, "units": units})

    def create_trailer(
        self,
        name: str,
        code: str,
        desc: str = "",
        phone: str = "",
        custom_fields: dict[str, str] | None = None,
    ) -> None:
        """
        Creates a trailer for the resource.

        :param name: A name for the new trailer.
        :type name: :py:obj:`str`
        :param code: A unique code for the new trailer.
        :type code: :py:obj:`str`
        :param desc: A description for the trailer.
        :type desc: :py:obj:`str`
        :param phone: A phone number beginning in a country code. No spaces.
        :type phone: :py:obj:`str`
        :param custom_fields: Additional custom fields to add to the trailer.
        :type custom_fields: :py:obj:`dict` | :py:obj:`None`
        :raises WialonError: If something goes wrong calling the Wialon API.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        params = {
            "itemId": self.id,
            "id": 0,
            "callMode": "create",
            "c": code,
            "ds": desc,
            "n": name,
            "f": 1,
        }
        if phone:
            params.update({"p": quote_plus(phone)})
        if custom_fields:
            params.update({"jp": custom_fields})
        self.session.wialon_api.resource_update_trailer(**params)
