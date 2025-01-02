from terminusgps.wialon import flags
from terminusgps.wialon.items.base import WialonBase


class WialonRetranslator(WialonBase):
    def create(self, **kwargs) -> int | None:
        if not kwargs.get("creator_id"):
            raise ValueError("'creator_id' is required on creation.")
        if not kwargs.get("name"):
            raise ValueError("'name' is required on creation.")
        if not kwargs.get("config"):
            raise ValueError("'config' is required on creation.")

        response = self.session.wialon_api.core_create_retranslator(
            **{
                "creatorId": kwargs["creator_id"],
                "name": kwargs["name"],
                "config": kwargs["config"],
                "dataFlags": flags.DATAFLAG_UNIT_BASE,
            }
        )
        return response.get("item", {}).get("id")
