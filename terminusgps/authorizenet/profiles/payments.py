from authorizenet.apicontractsv1 import (
    createCustomerPaymentProfileRequest,
    getCustomerPaymentProfileRequest,
    deleteCustomerPaymentProfileRequest,
    paymentProfile,
    validateCustomerPaymentProfileRequest,
)
from authorizenet.apicontrollers import (
    createCustomerPaymentProfileController,
    deleteCustomerPaymentProfileController,
    getCustomerPaymentProfileController,
    validateCustomerPaymentProfileController,
)
from terminusgps.authorizenet.profiles.base import AuthorizenetCustomerProfileBase


class PaymentProfile(AuthorizenetCustomerProfileBase):
    def create(self, **kwargs) -> int:
        """
        Creates an Authorize.NET payment profile.

        :param billing_address: A billing address for the payment profile.
        :type billing_address: :py:obj:`~authorizenet.apicontractsv1.customerAddressType`
        :param payment: An Authorize.NET API payment object. Usually a credit card, but could be a bank account.
        :type payment: :py:obj:`~authorizenet.apicontractsv1.paymentType`
        :param default: Whether or not the payment method should be marked as default. Default is :py:obj:`False`.
        :type default: :py:obj:`bool`
        :returns: The new payment profile id.
        :rtype: :py:obj:`int`

        """
        if not kwargs.get("billing_address"):
            raise ValueError("'billing_address' is required on creation.")
        if not kwargs.get("payment"):
            raise ValueError("'payment' is required on creation.")

        request = createCustomerPaymentProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            paymentProfile=paymentProfile(
                billTo=kwargs["billing_address"],
                payment=kwargs["payment"],
                defaultPaymentProfile=self.default,
            ),
            validationMode=self.validationMode,
        )
        controller = createCustomerPaymentProfileController(request)
        response = self.execute_controller(controller)
        return int(response.get("customerPaymentProfileId"))

    def delete(self) -> None:
        """Deletes the Authorize.NET payment profile."""
        request = deleteCustomerPaymentProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerPaymentProfileId=self.id,
        )
        controller = deleteCustomerPaymentProfileController(request)
        self.execute_controller(controller)

    def validate(self) -> None:
        """Validates the Authorize.NET payment profile."""
        request = validateCustomerPaymentProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerPaymentProfileId=self.id,
            validationMode=self.validationMode,
        )
        controller = validateCustomerPaymentProfileController(request)
        self.execute_controller(controller)

    def get_details(self, issuer_info: bool = False) -> dict:
        """
        Calls the Authorize.NET API and retrieves the payment profile.

        :param issuer_info: Whether or not Authorize.NET should return issuer info for the payment profile.
        :type issuer_info: :py:obj:`bool`
        :returns: The Authorize.NET API payment profile.
        :rtype: :py:obj:`~authorizenet.apicontractsv1.paymentProfile`

        """
        request = getCustomerPaymentProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerPaymentProfileId=self.id,
            includeIssuerInfo="true" if issuer_info else "false",
        )
        controller = getCustomerPaymentProfileController(request)
        response = self.execute_controller(controller)
        return response
