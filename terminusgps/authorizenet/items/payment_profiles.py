from authorizenet import apicontractsv1, apicontrollers

from .base import AuthorizenetBase


class AuthorizenetPaymentProfile(AuthorizenetBase):
    """An Authorizenet payment profile."""

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

    def _authorizenet_create_customer_payment_profile(
        self,
        payment: apicontractsv1.paymentType,
        address: apicontractsv1.customerAddressType,
        default: bool = False,
        validate: bool = False,
    ) -> int:
        request = apicontractsv1.createCustomerPaymentProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            paymentProfile=apicontractsv1.paymentProfileType(
                payment=payment,
                billTo=address,
                defaultPaymentProfile=str(default).lower(),
            ),
        )
        if validate:
            request.validationMode = self.validationMode

        controller = apicontrollers.createCustomerPaymentProfileController(request)
        response = self.execute_controller(controller)
        payment_profile_id: int = int(response.customerPaymentProfileId)
        self.id = payment_profile_id
        return payment_profile_id
