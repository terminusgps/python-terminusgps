from django.db import models
from django.utils.translation import gettext_lazy as _

ANET_XMLNS = "{AnetApi/xml/v1/schema/AnetApiSchema.xsd}"
"""Authorizenet XML namespace."""


class AuthorizenetSubscriptionStatus(models.TextChoices):
    """An Authorizenet subscription status."""

    ACTIVE = "active", _("Active")
    """Active subscription."""
    EXPIRED = "expired", _("Expired")
    """Expired subscription."""
    SUSPENDED = "suspended", _("Suspended")
    """Suspended subscription."""
    CANCELED = "canceled", _("Canceled")
    """Canceled subscription."""
    TERMINATED = "terminated", _("Terminated")
    """Terminated subscription."""
