Usage Examples
==============

===============================
Create a new unit and rename it
===============================

1. Import :py:obj:`~terminusgps.wialon.session.WialonSession` and :py:obj:`~terminusgps.wialon.items.WialonUnit`.

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

1. Import :py:obj:`~terminusgps.wialon.session.WialonSession` and :py:obj:`~terminusgps.wialon.items`.

.. code:: python

    from terminusgps.wialon.session import WialonSession
    from terminusgps.wialon import items

2. Create an account user.

.. code:: python

   with WialonSession(token="my_secure_wialon_token") as session:


-----------------
Full code example
-----------------

.. code:: python

    from django.conf import settings

    from terminusgps.wialon import items, constants
    from terminusgps.wialon.session import WialonSession
    from terminusgps.wialon.utils import generate_wialon_password, get_hw_type_id

    with WialonSession(token="my_secure_wialon_token") as session:
        hw_type_id = get_hw_type_id("Test HW", session)

        account_user = items.WialonUser(
            id=None,
            session=session,
            creator_id=settings.WIALON_ADMIN_ID,
            name="account_user",
            password=generate_wialon_password(32),
        )
        account_resource = items.WialonResource(
            id=None,
            session=session,
            creator_id=account_user.id, # Use the new account user to create this resource
            name="account_resource",
        )
        unit = WialonUnit(
            id=None,
            session=session,
            creator_id=settings.WIALON_ADMIN_ID, # Account user CANNOT create the unit
            name="test_unit",
            hw_type_id=hw_type_id,
        )

        account_user.grant_access(unit, access_mask=constants.ACCESSMASK_UNIT_MIGRATION)
        account_resource.migrate_unit(unit)
