from abc import abstractmethod

from terminusgps.wialon import flags
from terminusgps.wialon.session import WialonSession


class WialonObject:
    """Base class for Wialon objects."""

    def __init__(self, session: WialonSession, id: int | str | None = None) -> None:
        """
        Sets the session and id for the Wialon object.

        If ``id`` is :py:obj:`None` most methods will raise :py:exec:`AssertionError`.

        :param session: A valid Wialon API session.
        :type session: :py:obj:`~terminusgps.wialon.session.WialonSession`
        :param id: A Wialon object id. Default is :py:obj:`None`.
        :type id: :py:obj:`str` | :py:obj:`int` | :py:obj:`None`
        :raises ValueError: If ``id`` wasn't a digit.
        :returns: Nothing.
        :rtype: :py:obj:`None`

        """
        if isinstance(id, str) and not id.isdigit():
            raise ValueError(f"'id' must be a digit, got '{id}'.")
        self._session = session
        self._id = id

    def __str__(self) -> str:
        """Returns the Wialon object id as a string."""
        return str(self.id)

    def __repr__(self) -> str:
        """Returns the Wialon object type and parameters used to initialize it."""
        return f"{type(self).__name__}(id={self.id}, session={self.session.id})"

    @abstractmethod
    def create(self, *args, **kwargs) -> dict[str, str]:
        """Creates the Wialon object and sets its id."""
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def delete(self, *args, **kwargs) -> dict[str, str]:
        """Deletes the Wialon object."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def session(self) -> WialonSession:
        """Wialon object API session."""
        return self._session

    @property
    def id(self) -> int | None:
        """Wialon object id."""
        return int(self._id) if self._id is not None else None

    @id.setter
    def id(self, other: int | str | None = None) -> None:
        """Sets :py:attr:`_id` to ``other``."""
        self._id = other

    def set_admin_field(
        self, key: str, value: str, id: int | str | None = None
    ) -> dict[str, str]:
        """
        Sets an admin field for the Wialon object.

        If ``id`` isn't provided, a new admin field is created.

        :param key: An admin field key.
        :type key: :py:obj:`str`
        :param value: An admin field value.
        :type value: :py:obj:`str`
        :param id: An admin field id. Default is :py:obj:`None`.
        :type id: :py:obj:`int` | :py:obj:`str` | :py:obj:`None`
        :raises AssertionError: If the Wialon object id wasn't set.
        :raises WialonAPIError: If something went wrong calling the Wialon API.
        :returns: A dictionary of admin field data.
        :rtype: :py:obj:`dict`[:py:obj:`str`, :py:obj:`str`]

        """
        assert self.id, "Wialon object id wasn't set."
        if isinstance(id, str) and not id.isdigit():
            raise ValueError(f"'id' can only be digits, got '{id}'.")
        return self.session.wialon_api.item_update_admin_field(
            **{
                "itemId": self.id,
                "id": int(id) if id else 0,
                "callMode": "update" if id else "create",
                "n": key,
                "v": value,
            }
        )

    def set_custom_field(
        self, key: str, value: str, id: int | str | None = None
    ) -> dict[str, str]:
        """
        Sets a custom field for the Wialon object.

        If ``id`` isn't provided, a new custom field is created.

        :param key: A custom field key.
        :type key: :py:obj:`str`
        :param value: A custom field value.
        :type value: :py:obj:`str`
        :param id: A custom field id. Default is :py:obj:`None`.
        :type id: :py:obj:`int` | :py:obj:`str` | :py:obj:`None`
        :raises AssertionError: If the Wialon object id wasn't set.
        :raises WialonAPIError: If something went wrong calling the Wialon API.
        :returns: A dictionary of custom field data.
        :rtype: :py:obj:`dict`[:py:obj:`str`, :py:obj:`str`]

        """
        assert self.id, "Wialon object id wasn't set."
        if isinstance(id, str) and not id.isdigit():
            raise ValueError(f"'id' can only be digits, got '{id}'.")
        return self.session.wialon_api.item_update_custom_field(
            **{
                "itemId": self.id,
                "id": int(id) if id else 0,
                "callMode": "update" if id else "create",
                "n": key,
                "v": value,
            }
        )

    def set_profile_field(self, key: str, value: str) -> dict[str, str]:
        """
        Sets a profile field for the Wialon object.

        :param key: A profile field key.
        :type key: :py:obj:`str`
        :param value: A profile field value.
        :type value: :py:obj:`str`
        :raises AssertionError: If the Wialon object id wasn't set.
        :raises WialonAPIError: If something went wrong calling the Wialon API.
        :returns: A dictionary of profile field data.
        :rtype: :py:obj:`dict`[:py:obj:`str`, :py:obj:`str`]

        """
        assert self.id, "Wialon object id wasn't set."
        if isinstance(id, str) and not id.isdigit():
            raise ValueError(f"'id' can only be digits, got '{id}'.")
        return self.session.wialon_api.item_update_profile_field(
            **{"itemId": self.id, "n": key, "v": value}
        )

    def set_name(self, new_name: str) -> dict[str, str]:
        """
        Sets the Wialon object's name to the new name.

        :param new_name: A new name for the Wialon object.
        :type new_name: :py:obj:`str`
        :raises AssertionError: If the Wialon object id wasn't set.
        :raises WialonAPIError: If something went wrong calling the Wialon API.

        """
        assert self.id, "Wialon object id wasn't set."
        return self.session.wialon_api.item_update_name(
            **{"itemId": self.id, "name": new_name}
        )

    def add_log_record(
        self, action: str, new_value: str, old_value: str
    ) -> dict[str, str]:
        """
        Adds a log record for the Wialon object.

        :param action: A Wialon log action.
        :type action: :py:obj:`str`
        :param new_value: New log record value.
        :type new_value: :py:obj:`str`
        :param old_value: Old log record value.
        :type old_value: :py:obj:`str`
        :raises AssertionError: If the Wialon object id wasn't set.
        :raises WialonAPIError: If something went wrong calling the Wialon API.

        """
        assert self.id, "Wialon object id wasn't set."
        return self.session.wialon_api.item_add_log_record(
            **{
                "itemId": self.id,
                "action": action,
                "newValue": new_value,
                "oldValue": old_value,
            }
        )

    def get_name(self) -> str:
        """
        Returns the Wialon object's name.

        :raises AssertionError: If the Wialon object id wasn't set.
        :raises WialonAPIError: If something went wrong calling the Wialon API.
        :returns: The Wialon object's name.
        :rtype: :py:obj:`str`

        """
        assert self.id, "Wialon object id wasn't set."
        return str(
            self.session.wialon_api.core_search_item(
                **{"id": self.id, "flags": flags.DataFlag.UNIT_BASE}
            )
            .get("item")
            .get("nm")
        )
