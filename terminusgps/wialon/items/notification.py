from terminusgps.wialon.items.base import WialonBase


class WialonNotification(WialonBase):
    def create(
        self,
        resource_id: str | int,
        name: str,
        activation_time: int,
        deactivation_time: int,
        text: str | None = None,
        max_alarms: int = 0,
        interval: int = 0,
        lang: str = "en",
    ) -> int | None:
        if isinstance(resource_id, str) and not resource_id.isdigit():
            raise ValueError(f"'resource_id' must be a digit, got '{resource_id}'.")

        response = self.session.wialon_api.resource_update_notification(
            **{
                "itemId": resource_id,
                "id": 0,
                "callMode": "create",
                "n": name,
                "txt": text if text else name,
                "ta": activation_time,
                "td": deactivation_time,
                "ma": max_alarms,
                "mmtd": interval,
                "la": lang,
            }
        )
        return int(response[0].get("id")) if response else None
