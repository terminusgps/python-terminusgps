from terminusgps.wialon import flags
from terminusgps.wialon.items.base import WialonObject


class WialonUser(WialonObject):
    """A Wialon `user <https://help.wialon.com/en/wialon-hosting/user-guide/management-system/users>`_."""

    def create(self, creator_id: int | str, name: str, password: str) -> dict[str, str]:
        """
        Creates the user in Wialon and sets its id.

        :param creator_id: A Wialon user id to set as the new user's creator.
        :type creator_id: :py:obj:`int` | :py:obj:`str`
        :param name: Wialon user name.
        :type name: :py:obj:`str`
        :param password: Wialon user password.
        :type password: :py:obj:`str`
        :raises ValueError: If ``creator_id`` wasn't a digit.
        :raises WialonAPIError: If something went wrong calling the Wialon API.
        :returns: A Wialon object dictionary.
        :rtype: :py:obj:`dict`[:py:obj:`str`, :py:obj:`str`]

        """
        if isinstance(creator_id, str) and not creator_id.isdigit():
            raise ValueError(f"'creator_id' must be a digit, got '{creator_id}'.")
        response = self.session.wialon_api.core_create_user(
            **{
                "creatorId": int(creator_id),
                "name": name,
                "password": password,
                "dataFlags": flags.DataFlag.USER_BASE,
            }
        )
        self.id = int(response.get("item", {}).get("id"))
        return response

    def delete(self) -> dict[str, str]:
        """
        Deletes the user in Wialon.

        :raises AssertionError: If the Wialon user id wasn't set.
        :raises WialonAPIError: If something went wrong calling the Wialon API.
        :returns: An empty dictionary.
        :rtype: :py:obj:`dict`[:py:obj:`str`, :py:obj:`str`]

        """
        assert self.id, "Wialon user id wasn't set."
        return self.session.wialon_api.item_delete_item(**{"itemId": self.id})

    def get_access_rights(
        self, object_type: str, direct: bool = True, flags: int = 0x1
    ) -> dict[str, str]:
        """
        Returns a dictionary of Wialon objects the user has access to.

        :param object_type: A Wialon object type.
        :type object_type: :py:obj:`str`
        :param direct: Whether or not to exclude objects the user doesn't have direct access to. Default is :py:obj:`True`.
        :type direct: :py:obj:`bool`
        :param flags: Response flags. Default is ``0x1``.
        :type flags: :py:obj:`int`
        :raises AssertionError: If the Wialon user id wasn't set.
        :raises WialonAPIError: If something went wrong calling the Wialon API.
        :returns: A dictionary of Wialon objects.
        :rtype: :py:obj:`dict`[:py:obj:`str`, :py:obj:`str`]

        """
        assert self.id, "Wialon user id wasn't set."
        return self.session.wialon_api.user_get_items_access(
            **{
                "userId": self.id,
                "directAccess": int(direct),
                "itemSuperclass": object_type,
                "flags": flags,
            }
        )

    def set_access(self, object_id: int | str, access_mask: int) -> dict[str, str]:
        """
        Sets the user's access to ``object_id`` according to ``access_mask``.

        :param object_id: A Wialon object id.
        :type object_id: :py:obj:`int`
        :param access_mask: A Wialon access mask integer.
        :type access_mask: :py:obj:`int`
        :raises AssertionError: If the Wialon user id wasn't set.
        :raises ValueError: If the ``object_id`` wasn't a digit.
        :raises WialonAPIError: If something went wrong calling the Wialon API.
        :returns: An empty dictionary.
        :rtype: :py:obj:`dict`[:py:obj:`str`, :py:obj:`str`]

        """
        assert self.id, "Wialon user id wasn't set."
        if isinstance(object_id, str) and not object_id.isdigit():
            raise ValueError(f"'object_id' must be a digit, got '{object_id}'.")
        return self.session.wialon_api.user_update_item_access(
            **{"userId": self.id, "itemId": object_id, "accessMask": access_mask}
        )
