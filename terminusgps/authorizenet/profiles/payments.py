from authorizenet.apicontractsv1 import (
    createCustomerPaymentProfileRequest,
    customerAddressType,
    deleteCustomerPaymentProfileRequest,
    getCustomerPaymentProfileRequest,
    paymentProfile,
    paymentType,
    validateCustomerPaymentProfileRequest,
    updateCustomerPaymentProfileRequest,
)
from authorizenet.apicontrollers import (
    createCustomerPaymentProfileController,
    deleteCustomerPaymentProfileController,
    getCustomerPaymentProfileController,
    updateCustomerPaymentProfileController,
    validateCustomerPaymentProfileController,
)
from terminusgps.authorizenet.profiles.base import AuthorizenetCustomerProfileBase


class PaymentProfile(AuthorizenetCustomerProfileBase):
    def create(self, **kwargs) -> int:
        billing_addr = kwargs.get("billing_addr")
        payment = kwargs.get("payment")
        if not billing_addr:
            raise ValueError("'billing_addr' is required on creation.")
        if not payment:
            raise ValueError("'payment' is required on creation.")

        if not isinstance(billing_addr, customerAddressType):
            raise TypeError(
                f"'billing_addr' must be customerAddressType, got '{type(billing_addr)}'"
            )
        if not isinstance(payment, paymentType):
            raise TypeError(
                f"'payment' must be customerAddressType, got '{type(payment)}'"
            )

        return self._authorizenet_create_payment_profile(billing_addr, payment)

    def update(self, billing_addr: customerAddressType, payment: paymentType) -> None:
        self._authorizenet_update_payment_profile(billing_addr, payment)

    def delete(self) -> None:
        self._authorizenet_delete_payment_profile()

    def get_details(self, issuer_info: bool = False) -> dict:
        return self._authorizenet_get_payment_profile(issuer_info)

    def _authorizenet_create_payment_profile(
        self, billing_addr: customerAddressType, payment: paymentType
    ) -> int:
        """Executes a :py:obj:`~authorizenet.apicontractsv1.createCustomerPaymentProfileRequest` using the Authorize.NET API."""
        request = createCustomerPaymentProfileRequest(
            customerProfileId=self.customerProfileId,
            defaultPaymentProfile=self.default,
            merchantAuthentication=self.merchantAuthentication,
            paymentProfile=paymentProfile(billTo=billing_addr, payment=payment),
            validationMode=self.validationMode,
        )
        controller = createCustomerPaymentProfileController(request)
        response = self.execute_controller(controller)
        return int(response.customerPaymentProfileId)

    def _authorizenet_update_payment_profile(
        self, billing_addr: customerAddressType, payment: paymentType
    ) -> None:
        """Executes an :py:obj:`~authorizenet.apicontractsv1.updateCustomerPaymentProfileRequest` using the Authorize.NET API."""
        assert self.id, "'id' was not set."
        request = updateCustomerPaymentProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            paymentProfile=paymentProfile(
                billTo=billing_addr,
                payment=payment,
                defaultPaymentProfile=self.default,
                customerPaymentProfileId=self.id,
            ),
            validationMode=self.validationMode,
        )
        controller = updateCustomerPaymentProfileController(request)
        self.execute_controller(controller)

    def _authorizenet_get_payment_profile(self, issuer_info: bool = False) -> dict:
        """Executes a :py:obj:`~authorizenet.apicontractsv1.getCustomerPaymentProfileRequest` using the Authorize.NET API."""
        assert self.id, "'id' was not set."
        request = getCustomerPaymentProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerPaymentProfileId=self.id,
            includeIssuerInfo=str(issuer_info).lower(),
        )
        controller = getCustomerPaymentProfileController(request)
        return self.execute_controller(controller)

    def _authorizenet_validate_payment_profile(self) -> None:
        """Executes a :py:obj:`~authorizenet.apicontractsv1.validateCustomerPaymentProfileRequest` using the Authorize.NET API."""
        assert self.id, "'id' was not set."
        request = validateCustomerPaymentProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerPaymentProfileId=self.id,
            validationMode=self.validationMode,
        )
        controller = validateCustomerPaymentProfileController(request)
        self.execute_controller(controller)

    def _authorizenet_delete_payment_profile(self) -> None:
        """Executes a :py:obj:`~authorizenet.apicontractsv1.deleteCustomerPaymentProfileRequest` using the Authorize.NET API."""
        assert self.id, "'id' was not set."
        request = deleteCustomerPaymentProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerPaymentProfileId=self.id,
        )
        controller = deleteCustomerPaymentProfileController(request)
        self.execute_controller(controller)
