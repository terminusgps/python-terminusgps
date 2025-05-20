from .base import AuthorizenetBase


class AuthorizenetAddressProfile(AuthorizenetBase):
    """An Authorizenet address profile."""

    def __init__(
        self,
        customer_profile_id: int | str,
        id: int | str | None = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(id=id, *args, **kwargs)
        if isinstance(customer_profile_id, str) and not customer_profile_id.isdigit():
            raise ValueError(
                f"'customer_profile_id' can only contain digits, got '{customer_profile_id}'."
            )
        self.customerProfileId = customer_profile_id
