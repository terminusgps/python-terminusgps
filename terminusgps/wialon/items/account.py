from terminusgps.wialon.items.base import WialonBase
from terminusgps.wialon.items import WialonResource, WialonUser


class WialonAccount(WialonBase):
    def __init__(
        self, billing_plan: str = "terminusgps_ext_hist", *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.billing_plan = billing_plan

    def create(self, **kwargs) -> int | None:
        if not kwargs.get("creator_id"):
            raise ValueError("'creator_id' is required for creation.")

        user = WialonUser(id=str(kwargs["creator_id"]), session=self.session)
        resource = WialonResource(
            creator_id=kwargs["creator_id"],
            name=f"super_{user.name}",
            session=self.session,
        )
        self.session.wialon_api.account_create_account(
            **{"itemId": resource.id, "plan": kwargs.get("plan", self.billing_plan)}
        )
        return int(kwargs["resource_id"])
