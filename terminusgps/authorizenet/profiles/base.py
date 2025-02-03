from authorizenet.apicontractsv1 import merchantAuthenticationType
from ..auth import get_environment, get_merchant_auth, get_validation_mode


class AuthorizenetProfileBase:
    def __init__(
        self, merchant_id: int | str, id: int | str | None = None, **kwargs
    ) -> None:
        self.merchant_id = merchant_id
        self.id = str(id) if id else str(self.create(**kwargs))

    def __str__(self) -> str:
        return f"#{self.id}"

    @property
    def environment(self) -> str:
        return get_environment()

    @property
    def merchantAuthentication(self) -> merchantAuthenticationType:
        return get_merchant_auth()

    @property
    def validationMode(self) -> str:
        return get_validation_mode()

    @property
    def merchantCustomerId(self) -> str:
        return str(self.merchant_id)

    def create(self, **kwargs) -> int:
        raise NotImplementedError("Subclasses must implement this method.")

    def execute_controller(self, controller):
        controller.setenvironment(self.environment)
        controller.execute()
        response = controller.getresponse()
        if response.messages.resultCode != "Ok":
            raise ValueError(response.messages.message[0]["text"].text)
        return response


class AuthorizenetCustomerProfileBase(AuthorizenetProfileBase):
    def __init__(
        self, customer_profile_id: int | str, default: bool = False, **kwargs
    ) -> None:
        if isinstance(customer_profile_id, str) and not customer_profile_id.isdigit():
            raise ValueError(
                f"'customer_profile_id' must be a digit, got '{customer_profile_id}'."
            )

        self._default = default
        self.customer_profile_id = customer_profile_id
        return super().__init__(**kwargs)

    @property
    def customerProfileId(self) -> str:
        return str(self.customer_profile_id)

    @property
    def default(self) -> str:
        return str(self._default).lower()
