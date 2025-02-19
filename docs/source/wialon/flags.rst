Flags
=====

.. currentmodule:: terminusgps.wialon.flags

============
Access Flags
============

-------
General
-------

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#general>`_

.. py:data:: ACCESSFLAG_VIEW_ITEM_BASIC
.. py:data:: ACCESSFLAG_VIEW_ITEM_DETAILED
.. py:data:: ACCESSFLAG_MANAGE_ITEM_ACCESS
.. py:data:: ACCESSFLAG_DELETE_ITEM
.. py:data:: ACCESSFLAG_RENAME_ITEM
.. py:data:: ACCESSFLAG_VIEW_CUSTOM_FIELDS
.. py:data:: ACCESSFLAG_MANAGE_CUSTOM_FIELDS
.. py:data:: ACCESSFLAG_MANAGE_UNMENTIONED_FIELDS
.. py:data:: ACCESSFLAG_MANAGE_ICON
.. py:data:: ACCESSFLAG_QUERY_REPORTS
.. py:data:: ACCESSFLAG_MANAGE_ACL
.. py:data:: ACCESSFLAG_MANAGE_ITEM_LOG
.. py:data:: ACCESSFLAG_VIEW_ADMIN_FIELDS
.. py:data:: ACCESSFLAG_MANAGE_ADMIN_FIELDS
.. py:data:: ACCESSFLAG_VIEW_ATTACHED_FILES
.. py:data:: ACCESSFLAG_MANAGE_ATTACHED_FILES

---------------
Unit/Unit Group
---------------

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#units_and_unit_groups>`_

.. py:data:: ACCESSFLAG_UNIT_MANAGE_CONNECTIVITY
.. py:data:: ACCESSFLAG_UNIT_MANAGE_SENSORS
.. py:data:: ACCESSFLAG_UNIT_MANAGE_COUNTERS
.. py:data:: ACCESSFLAG_UNIT_DELETE_MESSAGES
.. py:data:: ACCESSFLAG_UNIT_EXECUTE_COMMANDS
.. py:data:: ACCESSFLAG_UNIT_REGISTER_EVENTS
.. py:data:: ACCESSFLAG_UNIT_VIEW_CONNECTIVITY
.. py:data:: ACCESSFLAG_UNIT_VIEW_SERVICE_INTERVALS
.. py:data:: ACCESSFLAG_UNIT_MANAGE_SERVICE_INTERVALS
.. py:data:: ACCESSFLAG_UNIT_IMPORT_MESSAGES
.. py:data:: ACCESSFLAG_UNIT_EXPORT_MESSAGES
.. py:data:: ACCESSFLAG_UNIT_VIEW_COMMANDS
.. py:data:: ACCESSFLAG_UNIT_MANAGE_COMMANDS
.. py:data:: ACCESSFLAG_UNIT_MANAGE_TRIP_DETECTOR
.. py:data:: ACCESSFLAG_UNIT_MANAGE_ASSIGNMENTS

----
User
----

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#users>`_

.. py:data:: ACCESSFLAG_USER_MANAGE_ACCESS_RIGHTS
.. py:data:: ACCESSFLAG_USER_ACT_AS_OTHER
.. py:data:: ACCESSFLAG_USER_MANAGE_FLAGS
.. py:data:: ACCESSFLAG_USER_VIEW_PUSH_MESSAGES
.. py:data:: ACCESSFLAG_USER_MANAGE_PUSH_MESSAGES

------------
Retranslator
------------

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#retranslators>`_

.. py:data:: ACCESSFLAG_RETRANSLATOR_MANAGE_PROPERTIES
.. py:data:: ACCESSFLAG_RETRANSLATOR_MANAGE_UNITS

------------------
Resources/Accounts 
------------------

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#resources_accounts>`_

.. py:data:: ACCESSFLAG_RESOURCE_VIEW_NOTIFICATIONS
.. py:data:: ACCESSFLAG_RESOURCE_MANAGE_NOTIFICATIONS
.. py:data:: ACCESSFLAG_RESOURCE_VIEW_POIS
.. py:data:: ACCESSFLAG_RESOURCE_MANAGE_POIS
.. py:data:: ACCESSFLAG_RESOURCE_VIEW_GEOFENCES
.. py:data:: ACCESSFLAG_RESOURCE_MANAGE_GEOFENCES
.. py:data:: ACCESSFLAG_RESOURCE_VIEW_JOBS
.. py:data:: ACCESSFLAG_RESOURCE_MANAGE_JOBS
.. py:data:: ACCESSFLAG_RESOURCE_VIEW_REPORT_TEMPLATES
.. py:data:: ACCESSFLAG_RESOURCE_MANAGE_REPORT_TEMPLATES
.. py:data:: ACCESSFLAG_RESOURCE_VIEW_DRIVERS
.. py:data:: ACCESSFLAG_RESOURCE_MANAGE_DRIVERS
.. py:data:: ACCESSFLAG_RESOURCE_MANAGE_ACCOUNT
.. py:data:: ACCESSFLAG_RESOURCE_VIEW_ORDERS
.. py:data:: ACCESSFLAG_RESOURCE_MANAGE_ORDERS
.. py:data:: ACCESSFLAG_RESOURCE_VIEW_TRAILERS
.. py:data:: ACCESSFLAG_RESOURCE_MANAGE_TRAILERS

------
Routes
------

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#routes>`_

.. py:data:: ACCESSFLAG_ROUTE_MANAGE_ROUTE

-----
Other
-----

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#other>`_

.. py:data:: ACCESSFLAG_FULL_ACCESS

==========
Data Flags
==========

------------
Retranslator
------------

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/retranslator>`_

.. py:data:: DATAFLAG_RETRANSLATOR_BASE
.. py:data:: DATAFLAG_RETRANSLATOR_CUSTOM_PROPERTIES
.. py:data:: DATAFLAG_RETRANSLATOR_BILLING_PROPERTIES
.. py:data:: DATAFLAG_RETRANSLATOR_GUID
.. py:data:: DATAFLAG_RETRANSLATOR_ADMIN_FIELDS
.. py:data:: DATAFLAG_RETRANSLATOR_CONFIGURATION
.. py:data:: DATAFLAG_RETRANSLATOR_UNITS
.. py:data:: DATAFLAG_RETRANSLATOR_ALL


-----------------
Resource/Accounts
-----------------

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/resource>`_

.. py:data:: DATAFLAG_RESOURCE_BASE
.. py:data:: DATAFLAG_RESOURCE_CUSTOM_PROPERTIES
.. py:data:: DATAFLAG_RESOURCE_BILLING_PROPERTIES
.. py:data:: DATAFLAG_RESOURCE_CUSTOM_FIELDS
.. py:data:: DATAFLAG_RESOURCE_MESSAGES
.. py:data:: DATAFLAG_RESOURCE_GUID
.. py:data:: DATAFLAG_RESOURCE_ADMIN_FIELDS
.. py:data:: DATAFLAG_RESOURCE_DRIVERS
.. py:data:: DATAFLAG_RESOURCE_JOBS
.. py:data:: DATAFLAG_RESOURCE_NOTIFICATIONS
.. py:data:: DATAFLAG_RESOURCE_POIS
.. py:data:: DATAFLAG_RESOURCE_GEOFENCES
.. py:data:: DATAFLAG_RESOURCE_REPORT_TEMPLATES
.. py:data:: DATAFLAG_RESOURCE_DRIVER_ATTACHABLE_UNITS
.. py:data:: DATAFLAG_RESOURCE_DRIVER_GROUPS
.. py:data:: DATAFLAG_RESOURCE_TRAILERS
.. py:data:: DATAFLAG_RESOURCE_TRAILER_GROUPS
.. py:data:: DATAFLAG_RESOURCE_TRAILER_ATTACHABLE_UNITS
.. py:data:: DATAFLAG_RESOURCE_ORDERS
.. py:data:: DATAFLAG_RESOURCE_GEOFENCE_GROUPS
.. py:data:: DATAFLAG_RESOURCE_TAGS
.. py:data:: DATAFLAG_RESOURCE_TAG_ATTACHABLE_UNITS
.. py:data:: DATAFLAG_RESOURCE_TAG_GROUPS
.. py:data:: DATAFLAG_RESOURCE_ALL

-----
Route
-----

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/route>`_

.. py:data:: DATAFLAG_ROUTE_BASE
.. py:data:: DATAFLAG_ROUTE_CUSTOM_PROPERTIES
.. py:data:: DATAFLAG_ROUTE_BILLING_PROPERTIES
.. py:data:: DATAFLAG_ROUTE_GUID
.. py:data:: DATAFLAG_ROUTE_ADMIN_FIELDS
.. py:data:: DATAFLAG_ROUTE_CONFIGURATION
.. py:data:: DATAFLAG_ROUTE_CHECKPOINTS
.. py:data:: DATAFLAG_ROUTE_SCHEDULES
.. py:data:: DATAFLAG_ROUTE_ROUNDS
.. py:data:: DATAFLAG_ROUTE_ALL

---------------
Unit/Unit Group
---------------

`Wialon API Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/unit>`_
