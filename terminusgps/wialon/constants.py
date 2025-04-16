import enum

from . import flags


class WialonItemsType(enum.StrEnum):
    """
    Wialon item types for Wialon API calls.

    `Wialon Item Types Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/search_items>`_

    """

    HARDWARE = "avl_hw"
    """Hardware type."""
    RESOURCE = "avl_resource"
    """Resource."""
    RETRANSLATOR = "avl_retranslator"
    """Retranslator."""
    ROUTE = "avl_route"
    """Route."""
    UNIT = "avl_unit"
    """Unit."""
    UNIT_GROUP = "avl_unit_group"
    """Unit group."""
    USER = "user"
    """User."""


class WialonItemProperty(enum.StrEnum):
    """
    Wialon item properties for Wialon API calls.

    `Wialon Item Property Reference <https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/search_items>`_

    """

    ACCOUNT_BALANCE = "sys_account_balance"
    """Current account balance."""
    ACCOUNT_BLOCKED = "sys_account_disabled"
    """Whether or not the account is blocked."""
    ACCOUNT_BLOCKED_TIME = "rel_account_disabled_mod_time"
    """Time (UNIX timestamp) the account was last blocked."""
    ACCOUNT_DAYS = "sys_account_days"
    """Number of days on the account."""
    ACCOUNT_DEALER_RIGHTS = "sys_account_enable_parent"
    """Whether or not the account has dealer rights."""
    ACCOUNT_ID = "sys_billing_account_guid"
    """Account id."""
    ACCOUNT_NAME = "rel_billing_account_name"
    """Account name."""
    ACCOUNT_NUM_UNITS = "rel_account_units_usage"
    """Number of units in the account."""
    ACCOUNT_PARENT_NAME = "rel_billing_parent_account_name"
    """Parent account name for the account."""
    ACCOUNT_PLAN_NAME = "rel_billing_plan_name"
    """Billing plan assigned to the account."""
    ADMIN_FIELD_NAME = "rel_adminfield_name"
    """Admin field name."""
    ADMIN_FIELD_NAME_VALUE = "rel_adminfield_name_value"
    """Admin field name/value, format: ``'name:value'``."""
    ADMIN_FIELD_VALUE = "rel_adminfield_value"
    """Admin field value."""
    CREATION_TIME = "rel_creation_time"
    """Time (UNIX timestamp) the object was created."""
    CREATOR_ID = "sys_user_creator"
    """Creator user id."""
    CREATOR_NAME = "rel_user_creator_name"
    """Creator user name."""
    CUSTOM_FIELD_NAME = "rel_customfield_name"
    """Custom field name."""
    CUSTOM_FIELD_NAME_VALUE = "rel_customfield_name_value"
    """Custom field name/value, format: ``'name:value'``."""
    CUSTOM_FIELD_VALUE = "rel_customfield_value"
    """Custom field value."""
    GROUP_NUM_UNITS = "rel_group_unit_count"
    """Number of units in the group."""
    HARDWARE_ID = "rel_hw_type_id"
    """Hardware id."""
    HARDWARE_NAME = "rel_hw_type_name"
    """Hardware name."""
    HARDWARE_STATE = "sys_comm_state"
    """Hardware state."""
    ID = "sys_id"
    """Object id."""
    LAST_LOGIN_TIME = "login_date"
    """Time (UNIX timestamp) the user last logged in."""
    LAST_MESSAGE_TIME = "rel_last_msg_date"
    """Time (UNIX timestamp) of the last message."""
    NAME = "sys_name"
    """Object name."""
    PHONE = "sys_phone_number"
    """Object phone number."""
    PHONE2 = "sys_phone_number2"
    """Secondary (optional) object phone number."""
    PROFILE_FIELD = "profilefield"
    """Profile field."""
    PROFILE_FIELD_NAME = "rel_profilefield_name"
    """Profile field name."""
    PROFILE_FIELD_NAME_VALUE = "rel_profilefield_name_value"
    """Profile field name/value, format: ``'name:value'``"""
    PROFILE_FIELD_VALUE = "rel_profilefield_value"
    """Profile field value."""
    RESOURCE_IS_ACCOUNT = "rel_is_account"
    """Whether or not the resource is an account."""
    RETRANSLATOR_ENABLED = "retranslator_enabled"
    """Whether or not a retranslator is enabled."""
    UNIQUE_ID = "sys_unique_id"
    """Object unique id."""


ACCESSMASK_RESOURCE_BASIC: int = sum(
    [
        flags.AccessFlag.MANAGE_CUSTOM_FIELDS,
        flags.AccessFlag.RESOURCE_MANAGE_DRIVERS,
        flags.AccessFlag.RESOURCE_MANAGE_GEOFENCES,
        flags.AccessFlag.RESOURCE_MANAGE_NOTIFICATIONS,
        flags.AccessFlag.RESOURCE_VIEW_DRIVERS,
        flags.AccessFlag.RESOURCE_VIEW_GEOFENCES,
        flags.AccessFlag.RESOURCE_VIEW_NOTIFICATIONS,
        flags.AccessFlag.RESOURCE_VIEW_ORDERS,
        flags.AccessFlag.RESOURCE_VIEW_POIS,
        flags.AccessFlag.RESOURCE_VIEW_TRAILERS,
        flags.AccessFlag.VIEW_ADMIN_FIELDS,
        flags.AccessFlag.VIEW_CUSTOM_FIELDS,
        flags.AccessFlag.VIEW_ITEM_BASIC,
    ]
)
"""Basic resource permissions"""

ACCESSMASK_UNIT_BASIC: int = sum(
    [
        flags.AccessFlag.MANAGE_CUSTOM_FIELDS,
        flags.AccessFlag.MANAGE_ICON,
        flags.AccessFlag.QUERY_REPORTS,
        flags.AccessFlag.RENAME_ITEM,
        flags.AccessFlag.UNIT_EXECUTE_COMMANDS,
        flags.AccessFlag.UNIT_EXPORT_MESSAGES,
        flags.AccessFlag.UNIT_IMPORT_MESSAGES,
        flags.AccessFlag.UNIT_REGISTER_EVENTS,
        flags.AccessFlag.UNIT_VIEW_SERVICE_INTERVALS,
        flags.AccessFlag.VIEW_ATTACHED_FILES,
        flags.AccessFlag.VIEW_CUSTOM_FIELDS,
        flags.AccessFlag.VIEW_ITEM_BASIC,
        flags.AccessFlag.VIEW_ITEM_DETAILED,
    ]
)
"""Basic unit permissions"""

ACCESSMASK_UNIT_MIGRATION: int = sum(
    [
        flags.AccessFlag.DELETE_ITEM,
        flags.AccessFlag.MANAGE_ITEM_ACCESS,
        flags.AccessFlag.UNIT_DELETE_MESSAGES,
        flags.AccessFlag.UNIT_MANAGE_CONNECTIVITY,
        flags.AccessFlag.VIEW_ITEM_BASIC,
    ]
)
"""Unit migration permissions"""
