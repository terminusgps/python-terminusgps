from terminusgps.wialon import flags

ACCESSMASK_UNIT_BASIC: int = sum(
    [
        flags.ACCESSFLAG_VIEW_ITEM_BASIC,
        flags.ACCESSFLAG_VIEW_ITEM_DETAILED,
        flags.ACCESSFLAG_RENAME_ITEM,
        flags.ACCESSFLAG_VIEW_CUSTOM_FIELDS,
        flags.ACCESSFLAG_MANAGE_CUSTOM_FIELDS,
        flags.ACCESSFLAG_MANAGE_ICON,
        flags.ACCESSFLAG_QUERY_REPORTS,
        flags.ACCESSFLAG_VIEW_ATTACHED_FILES,
        flags.ACCESSFLAG_UNIT_EXECUTE_COMMANDS,
        flags.ACCESSFLAG_UNIT_VIEW_SERVICE_INTERVALS,
        flags.ACCESSFLAG_UNIT_REGISTER_EVENTS,
        flags.ACCESSFLAG_UNIT_IMPORT_MESSAGES,
        flags.ACCESSFLAG_UNIT_EXPORT_MESSAGES,
    ]
)

ACCESSMASK_UNIT_SUPER: int = sum(
    [
        flags.ACCESSFLAG_VIEW_ITEM_BASIC,
        flags.ACCESSFLAG_VIEW_ITEM_DETAILED,
        flags.ACCESSFLAG_RENAME_ITEM,
        flags.ACCESSFLAG_VIEW_CUSTOM_FIELDS,
        flags.ACCESSFLAG_MANAGE_CUSTOM_FIELDS,
        flags.ACCESSFLAG_MANAGE_ICON,
        flags.ACCESSFLAG_QUERY_REPORTS,
        flags.ACCESSFLAG_VIEW_ATTACHED_FILES,
        flags.ACCESSFLAG_UNIT_EXECUTE_COMMANDS,
        flags.ACCESSFLAG_UNIT_VIEW_SERVICE_INTERVALS,
        flags.ACCESSFLAG_UNIT_REGISTER_EVENTS,
        flags.ACCESSFLAG_UNIT_IMPORT_MESSAGES,
        flags.ACCESSFLAG_UNIT_EXPORT_MESSAGES,
    ]
)

ACCESSMASK_UNIT_FULL: int = sum([flags.ACCESSFLAG_FULL_ACCESS])
