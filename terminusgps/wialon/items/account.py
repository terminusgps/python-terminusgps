from terminusgps.wialon.items.base import WialonBase


class WialonAccount(WialonBase):
    def __init__(
        self, billing_plan: str = "terminusgps_ext_hist", *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.billing_plan = billing_plan

    def create(self, **kwargs) -> int | None:
        if not kwargs.get("resource_id"):
            raise ValueError("'resource_id' is required for creation.")

        self.session.wialon_api.account_create_account(
            **{
                "itemId": kwargs["resource_id"],
                "plan": kwargs.get("plan", self.billing_plan),
            }
        )
        return int(kwargs["resource_id"])
