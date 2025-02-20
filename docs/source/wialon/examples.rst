Usage Examples
==============

===============================
Create a new unit and rename it
===============================

1. Import :py:obj:`~terminusgps.wialon.session.WialonSession` and :py:obj:`~terminusgps.wialon.items.unit.WialonUnit`.

Let's also import :py:obj:`~terminusgps.wialon.utils.generate_wialon_password` so we don't have to come up with a valid Wialon password ourselves.

.. code:: python

    from terminusgps.wialon.session import WialonSession
    from terminusgps.wialon.items import WialonUnit
    from terminusgps.wialon.utils import generate_wialon_password

2. Open the session in a context manager and instantiate a unit.

.. code:: python

    with WialonSession(token="my_wialon_api_token") as session:
        unit = WialonUnit(
            id=None,
            session=session,
            creator_id="123",
            name="test_user",
            password=generate_wialon_password(32)
        )
        print(f"{unit.name = }") # unit.name = "test_user"

3. Within the context manager, :py:obj:`~terminusgps.wialon.items.WialonUnit` methods can be executed.

.. code:: python

    with WialonSession(token="my_secure_wialon_token") as session:
        ...

        unit.rename("super_test_user")
        # Session is logged out after exiting scope

-----------------
Full code example
-----------------

.. code:: python

    from terminusgps.wialon.session import WialonSession
    from terminusgps.wialon.items import WialonUnit
    from terminusgps.wialon.utils import generate_wialon_password

    with WialonSession(token="my_secure_wialon_token") as session:
        unit = WialonUnit(
            id=None,
            session=session,
            creator_id="123",
            name="test_user",
            password=generate_wialon_password(32)
        )
        unit.rename("super_test_user")


============================================
Create an account and migrate a unit into it
============================================

1. Import :py:obj:`~terminusgps.wialon.session.WialonSession`, :py:mod:`~terminusgps.wialon.items`, and :py:mod:`~terminusgps.wialon.constants`.

.. code:: python

    from terminusgps.wialon.session import WialonSession
    from terminusgps.wialon import items, constants

2. Create an account user.

.. code:: python

    with WialonSession(token="my_secure_wialon_token") as session:
        account_user = items.WialonUser(
            id=None,
            session=session,
            creator_id="27884511", # Admin user id
            name="account_user",
            password="super_secure_password1!",
        )

3. Create a resource using the account user.

.. code:: python

    with WialonSession(token="my_secure_wialon_token") as session:
        ...
        account_resource = items.WialonResource(
            id=None,
            session=session,
            creator_id=account_user.id,
            name="account_resource",
        )

4. Retrieve a :py:obj:`~terminusgps.wialon.items.unit.WialonUnit`.

.. code:: python

    with WialonSession(token="my_secure_wialon_token") as session:
        ...
        unit = items.WialonUnit(id="12345678", session=session)

5. Grant the account user migration permissions.

.. code:: python

    with WialonSession(token="my_secure_wialon_token") as session:
        ...
        account_user.grant_access(unit, access_mask=constants.ACCESSMASK_UNIT_MIGRATION)

6. Transform the resource into an account and enable it.

.. code:: python

    with WialonSession(token="my_secure_wialon_token") as session:
        ...
        account_resource.create_account("terminusgps_ext_hist")
        account_resource.enable()

7. Migrate the unit into the account.

.. code:: python

    with WialonSession(token="my_secure_wialon_token") as session:
        ...
        account_resource.migrate_unit(unit)


-----------------
Full code example
-----------------

.. code:: python

    from terminusgps.wialon.session import WialonSession
    from terminusgps.wialon import items, constants

    with WialonSession(token="my_secure_wialon_token") as session:
        account_user = items.WialonUser(
            id=None,
            session=session,
            creator_id="27884511", # Admin user id
            name="account_user",
            password="super_secure_password1!",
        )
        account_resource = items.WialonResource(
            id=None,
            session=session,
            creator_id=account_user.id,
            name="account_resource",
        )
        unit = items.WialonUnit(id="12345678", session=session)
        account_user.grant_access(unit, access_mask=constants.ACCESSMASK_UNIT_MIGRATION)
        account_resource.create_account("terminusgps_ext_hist")
        account_resource.enable()
        account_resource.migrate_unit(unit)
