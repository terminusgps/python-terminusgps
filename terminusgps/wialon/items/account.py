from terminusgps.wialon.items.base import WialonBase


class WialonAccount(WialonBase):
    def create(self, **kwargs) -> int | None:
        if not kwargs.get("resource_id"):
            raise ValueError("'resource_id' is required for creation.")

        self.session.wialon_api.account_create_account(
            **{
                "itemId": kwargs["resource_id"],
                "plan": kwargs.get("plan", "terminusgps_ext_hist"),
            }
        )
        return int(kwargs["resource_id"])
