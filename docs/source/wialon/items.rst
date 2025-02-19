Items
=====

.. currentmodule:: terminusgps.wialon.items.base

.. py:class:: WialonBase

    Base class for Wialon API objects.

    .. py:method:: create() -> int | None

        Creates a Wialon object and returns its id.
        
        :meta abstract:
        :returns: The new object's id.
        :rtype: :py:obj:`int` | :py:obj:`None`

    .. py:method:: rename(new_name) -> None

        Renames the Wialon object to the new name.

        :param new_name: A new name.
        :type new_name: :py:obj:`str`
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: add_afield(field) -> None

        Adds an admin field to the Wialon object.

        :param field: A tuple containing the name of the field and the value of the field.
        :type field: :py:obj:`tuple`
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: update_afield(field_id, field) -> None

        Updates an admin field by id to the Wialon object.

        :param field_id: The admin field id.
        :type field_id: :py:obj:`int`
        :param field: A tuple containing the name of the field and the value of the field.
        :type field: :py:obj:`tuple`
        :returns: Nothing.
        :rtype: :py:obj:`None`


    .. py:method:: add_cfield(field) -> None

        Adds a custom field to the Wialon object.

        :param field: A tuple containing the name of the field and the value of the field.
        :type field: :py:obj:`tuple`
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: update_cfield(field_id, field) -> None

        Updates a custom field by id.

        :param field_id: The admin field id.
        :type field_id: :py:obj:`int`
        :param field: A tuple containing the name of the field and the value of the field.
        :type field: :py:obj:`tuple`
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: add_cproperty(property) -> None

        Adds a custom property to the Wialon object.

        :param property: A tuple containing the name of the property and the value of the property.
        :type property: :py:obj:`tuple`
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: add_profile_field(field) -> None

        Adds a profile field to the Wialon object.

        :param field: A tuple containing the name of the field and the value of the field.
        :type field: :py:obj:`tuple`
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: delete() -> None

        Deletes the Wialon object.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`


.. currentmodule:: terminusgps.wialon.items.geofence

.. py:class:: WialonGeofence

.. currentmodule:: terminusgps.wialon.items.notification

.. py:class:: WialonNotification

.. currentmodule:: terminusgps.wialon.items.resource

.. py:class:: WialonResource

    .. py:method:: create(creator_id, name) -> int | None

        Creates a new Wialon resource.

        :param creator_id: A Wialon user id.
        :type creator_id: :py:obj:`int` | :py:obj:`str`
        :param name: A name for the resource.
        :type name: :py:obj:`str`
        :raises ValueError: If ``creator_id`` is not a digit.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: The Wialon id for the new resource, if it was created.
        :rtype: :py:obj:`int` | :py:obj:`None`

    .. py:method:: delete() -> None

        Deletes all micro-objects assigned to the resource.

        If the resource is an account, instead deletes all macro-objects and micro-objects assigned to the account.

        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: is_migrated(unit) -> None

        Checks if a unit is migrated into the account.

        :param unit: A Wialon object.
        :type unit: :py:obj:`~terminusgps.wialon.items.base.WialonBase`
        :returns: Whether or not the unit is migrated into the account.
        :rtype: :py:obj:`bool`

    .. py:method:: set_dealer_rights(enabled) -> None

        Sets dealer rights on the account.

        You **probably don't** need to use this method.

        :param enabled: :py:obj:`True` to enable dealer rights, :py:obj:`False` to disable dealer rights. Default is :py:obj:`False`.
        :type enabled: :py:obj:`bool`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: migrate_unit(unit) -> None

        Migrates a :py:obj:`WialonUnit` into the account.

        :param unit: A Wialon object.
        :type unit: :py:obj:`~terminusgps.wialon.items.base.WialonBase`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: update_plan(new_plan) -> None

        Updates the account billing plan.

        :param new_plan: The name of a billing plan.
        :type new_plan: :py:obj:`str`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: create_account(billing_plan) -> None

        Transforms the resource into an account.
    
        :param billing_plan: The name of a billing plan.
        :type billing_plan: :py:obj:`str`
        :raises AssertionError: If the resource is already account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: delete_account() -> None

        Deletes the account if it exists, as well as any micro-objects and macro-objects it contains.

        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: enable_account() -> None

        Enables the Wialon account.

        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: disable_account() -> None

        Disables the Wialon account.

        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: set_minimum_days([days=0]) -> None

        Sets the minimum days counter value to ``days``.

        :param days: Number of days to set the counter to. Default is ``0``.
        :type days: :py:obj:`int`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: add_days([days=30]) -> None

        Adds days to the account.

        :param days: Number of days to add to the account. Default is ``30``.
        :type days: :py:obj:`int`
        :raises AssertionError: If the resource is not an account.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: set_settings_flags([flags=0x20, block_balance_val=0.00, deny_balance_val=0.00]) -> None

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

    .. py:property:: is_dealer

        Whether or not the resource/account has dealer rights.

        :type: :py:obj:`bool`

    .. py:property:: is_account

        Whether or not the resource is an account.

        :type: :py:obj:`bool`

.. currentmodule:: terminusgps.wialon.items.retranslator

.. py:class:: WialonRetranslator

    .. py:method:: create(creator_id, name) -> int | None

        Creates a new Wialon route.

        :param creator_id: A Wialon user id.
        :type creator_id: :py:obj:`str` | :py:obj:`int`
        :param name: A name for the route.
        :type name: :py:obj:`str`
        :raises ValueError: If ``creator_id`` is not a digit.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: The Wialon id for the new route, if it was created.
        :rtype: :py:obj:`int` | :py:obj:`None`

.. currentmodule:: terminusgps.wialon.items.unit

.. py:class:: WialonUnit

    .. py:method:: create(creator_id, name, hw_type_id) -> int | None

        Creates a new Wialon unit.

        :param creator_id: A Wialon user id.
        :type creator_id: :py:obj:`str` | :py:obj:`int`
        :param name: A name for the unit.
        :type name: :py:obj:`str`
        :param hw_type_id: A Wialon hardware type ID.
        :type hw_type_id: :py:obj:`str` | :py:obj:`int`
        :returns: The Wialon id for the new unit.
        :rtype: :py:obj:`int` | :py:obj:`None`

    .. py:method:: execute_command(name, link_type, [timeout=5, flags=0, param=None]) -> None

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

    .. py:method:: set_access_password(password) -> None 

        Sets a new access password for this Wialon unit.

        :param password: A new access password.
        :type name: :py:obj:`str`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: activate() -> None

        Activates the Wialon unit.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: deactivate() -> None

        Deactivates the Wialon unit.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: assign_phone(phone) -> None

        Assigns a phone number to the Wialon unit.

        :param phone: A phone number beginning with a country code.
        :type phone: :py:obj:`str`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: get_phone_numbers() -> list[str]

        Retrieves all phone numbers assigned to the unit.

        This includes any attached drivers, custom/admin fields, or otherwise assigned phone numbers.

        :raises WialonError: If something goes wrong with Wialon.
        :returns: A list of phone numbers.
        :rtype: :py:obj:`list`

    .. py:property:: imei_number

        Unique id for the unit.
        
        :type: :py:obj:`int` | :py:obj:`None`

    .. py:property:: image_uri

        Unit image universal resource identifier.
        
        :type: :py:obj:`str`

    .. py:property:: active

        Whether or not the unit is activated in Wialon.
        
        :type: :py:obj:`bool`

.. currentmodule:: terminusgps.wialon.items.unit_group

.. py:class:: WialonUnitGroup

    .. py:method:: create(creator_id, name) -> int | None

        Creates a new Wialon unit group.

        :param creator_id: A Wialon user id.
        :type creator_id: :py:obj:`str` | :py:obj:`int`
        :param name: A name for the group.
        :type name: :py:obj:`str`
        :raises ValueError: If ``creator_id`` is not a digit.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: The Wialon id for the new group, if it was created.
        :rtype: :py:obj:`int` | :py:obj:`None`

    .. py:method:: set_items(new_items) -> None

        Sets this group's members to a list of Wialon unit ids.

        :param new_items: A list of Wialon unit ids.
        :type new_items: :py:obj:`list`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: is_member(item) -> bool

        Determines whether or not ``item`` is a member of the group.

        :param item: A Wialon object.
        :type item: :py:obj:`~terminusgps.wialon.items.base.WialonBase`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: :py:obj:`True` if ``item`` is a member of the group, else :py:obj:`False`.
        :rtype: :py:obj:`bool`

    .. py:method:: add_item(item) -> bool

        Adds a Wialon item to the group.

        :param item: A Wialon object.
        :type item: :py:obj:`~terminusgps.wialon.items.base.WialonBase`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:method:: rm_item(item) -> bool

        Removes a Wialon unit from the group, if it's a member of the group.

        :param item: A Wialon object.
        :type item: :py:obj:`~terminusgps.wialon.items.base.WialonBase`
        :raises AssertionError: If the item wasn't in the group.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py:property:: items

        A list of Wialon object ids in the group.

        :type: :py:obj:`list`

.. currentmodule:: terminusgps.wialon.items.user

.. py:class:: WialonUser

    .. py::method:: create(creator_id, name, password) -> int | None

        Creates a new Wialon user.

        :param creator_id: A Wialon user id.
        :type creator_id: :py:obj:`str` | :py:obj:`int`
        :param name: A name for the user.
        :type name: :py:obj:`str`
        :param password: A password for the user.
        :type password: :py:obj:`str`
        :raises ValueError: If ``creator_id`` is not a digit.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: The Wialon id for the new user, if it was created.
        :rtype: :py:obj:`int` | :py:obj:`None`

    .. py::method:: has_access(other) -> bool

        Checks if the user has access to ``other``.

        :param other: A Wialon object.
        :type phone: :py:obj:`~terminusgps.wialon.items.base.WialonBase`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: :py:obj:`True` if the user can access ``other``, else :py:obj:`False`.
        :rtype: :py:obj:`bool`

    .. py::method:: assign_phone(phone) -> None

        Assigns a phone number to the user.

        :param phone: A phone number, including country code.
        :type phone: :py:obj:`str`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py::method:: assign_email(email) -> None

        Assigns an email address to the user.

        :param phone: An email address.
        :type phone: :py:obj:`str`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py::method:: grant_access(item) -> None

        Grants the user access to ``item``.

        :param item: A Wialon object.
        :type item: :py:obj:`~terminusgps.wialon.items.base.WialonBase`
        :param access_mask: A Wialon access mask integer.
        :type access_mask: :py:obj:`int`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py::method:: set_settings_flags(flags, flags_mask) -> None

        Sets the user's settings flags.

        :param flags: The new user settings flags.
        :type flags: :py:obj:`int`
        :param flags_mask: A user settings flag mask.
        :type flags_mask: :py:obj:`int`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py::method:: update_password(old_password, new_password) -> None

        Updates the password of the user.

        :param old_password: The user's original password.
        :type old_password: :py:obj:`str`
        :param new_password: A new password.
        :type new_password: :py:obj:`str`
        :raises WialonError: If something goes wrong with Wialon.
        :returns: Nothing.
        :rtype: :py:obj:`None`

    .. py::method:: verify_auth(destination, [method="email"]) -> None

        Sends an authentication code to ``destination`` via ``method``.

        ``Method`` can be ``"email"`` or ``"sms"``.

        :param destination: The email or phone number to send an auth code to.
        :type destination: :py:obj:`str`
        :param method: Email or sms. Default is ``"email"``.
        :type method: :py:obj:`str`
        :raises ValueError: If the method isn't ``"email"`` or ``"sms"``.
        :raises WialonError: If something goes wrong with Wialon.
        :returns: An auth code.
        :rtype: :py:obj:`str`
