from unittest import TestCase

from terminusgps.wialon import constants, flags


class WialonConstantTestCase(TestCase):
    def test_accessmask_resource_basic(self):
        """Fails if :py:data:`ACCESSMASK_RESOURCE_BASIC` wasn't the expected flag."""
        const = constants.ACCESSMASK_RESOURCE_BASIC
        self.assertEqual(
            const,
            (
                flags.AccessFlag.MANAGE_CUSTOM_FIELDS
                | flags.AccessFlag.RESOURCE_MANAGE_DRIVERS
                | flags.AccessFlag.RESOURCE_MANAGE_GEOFENCES
                | flags.AccessFlag.RESOURCE_MANAGE_NOTIFICATIONS
                | flags.AccessFlag.RESOURCE_VIEW_DRIVERS
                | flags.AccessFlag.RESOURCE_VIEW_GEOFENCES
                | flags.AccessFlag.RESOURCE_VIEW_NOTIFICATIONS
                | flags.AccessFlag.RESOURCE_VIEW_ORDERS
                | flags.AccessFlag.RESOURCE_VIEW_POIS
                | flags.AccessFlag.RESOURCE_VIEW_TRAILERS
                | flags.AccessFlag.VIEW_ADMIN_FIELDS
                | flags.AccessFlag.VIEW_CUSTOM_FIELDS
                | flags.AccessFlag.VIEW_ITEM_BASIC
            ),
        )

    def test_accessmask_unit_basic(self):
        """Fails if :py:data:`ACCESSMASK_UNIT_BASIC` wasn't the expected flag."""
        const = constants.ACCESSMASK_UNIT_BASIC
        self.assertEqual(
            const,
            (
                flags.AccessFlag.MANAGE_CUSTOM_FIELDS
                | flags.AccessFlag.MANAGE_ICON
                | flags.AccessFlag.QUERY_REPORTS
                | flags.AccessFlag.RENAME_ITEM
                | flags.AccessFlag.UNIT_EXECUTE_COMMANDS
                | flags.AccessFlag.UNIT_EXPORT_MESSAGES
                | flags.AccessFlag.UNIT_IMPORT_MESSAGES
                | flags.AccessFlag.UNIT_REGISTER_EVENTS
                | flags.AccessFlag.UNIT_VIEW_SERVICE_INTERVALS
                | flags.AccessFlag.VIEW_ATTACHED_FILES
                | flags.AccessFlag.VIEW_CUSTOM_FIELDS
                | flags.AccessFlag.VIEW_ITEM_BASIC
                | flags.AccessFlag.VIEW_ITEM_DETAILED
            ),
        )

    def test_accessmask_unit_migration(self):
        """Fails if :py:data:`ACCESSMASK_UNIT_MIGRATION` wasn't the expected flag."""
        const = constants.ACCESSMASK_UNIT_MIGRATION
        self.assertEqual(
            const,
            (
                flags.AccessFlag.DELETE_ITEM
                | flags.AccessFlag.MANAGE_ITEM_ACCESS
                | flags.AccessFlag.UNIT_DELETE_MESSAGES
                | flags.AccessFlag.UNIT_MANAGE_CONNECTIVITY
                | flags.AccessFlag.VIEW_ITEM_BASIC
            ),
        )
