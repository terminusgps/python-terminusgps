from authorizenet.apicontrollers import (
    createCustomerProfileController,
    deleteCustomerProfileController,
    getCustomerProfileController,
    updateCustomerProfileController,
)
from authorizenet.apicontractsv1 import (
    customerProfileType,
    createCustomerProfileRequest,
    deleteCustomerProfileRequest,
    getCustomerProfileRequest,
    updateCustomerProfileRequest,
)

from terminusgps.authorizenet.profiles.base import AuthorizenetProfileBase


class CustomerProfile(AuthorizenetProfileBase):
    def create(self, **kwargs) -> int:
        """
        Creates the customer profile.

        :param email: An email address for the customer profile.
        :type email: :py:obj:`str`
        :param desc: A description describing the customer profile. Optional.
        :type desc: :py:obj:`str` | :py:obj:`None`
        :returns: The new customer profile id.
        :rtype: :py:obj:`int`

        """
        if not kwargs.get("email"):
            raise ValueError("'email' is required for creation.")

        return self._authorizenet_create_customer_profile(
            kwargs["email"], kwargs.get("desc", "")
        )

    def update(self, email: str, desc: str = "") -> None:
        """Updates the customer profile."""
        return self._authorizenet_update_customer_profile(email, desc)

    def delete(self) -> None:
        """Deletes the customer profile."""
        return self._authorizenet_delete_customer_profile()

    def get_payment_profiles(self) -> list[dict] | None:
        """Retrieves the customer profile's payment profiles list."""
        profiles = self._authorizenet_get_customer_profile(issuer_info=False).get(
            "paymentProfiles"
        )
        return profiles if profiles else None

    def get_shipping_addresses(self) -> list[dict] | None:
        """Retrieves the customer profile's shipping address list."""
        addresses = self._authorizenet_get_customer_profile(issuer_info=False).get(
            "shipToList"
        )
        return addresses if addresses else None

    def _authorizenet_create_customer_profile(self, email: str, desc: str = "") -> int:
        """Executes a :py:obj:`~authorizenet.apicontractsv1.createCustomerProfileRequest` using the Authorize.NET API."""
        request = createCustomerProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            profile=customerProfileType(
                merchantCustomerId=self.merchantCustomerId,
                email=email,
                description=desc,
            ),
        )
        controller = createCustomerProfileController(request)
        response = self.execute_controller(controller)
        return int(response.customerProfileId)

    def _authorizenet_delete_customer_profile(self) -> None:
        """Executes a :py:obj:`~authorizenet.apicontractsv1.deleteCustomerProfileRequest` using the Authorize.NET API."""
        assert self.id, "'id' was not set."
        request = deleteCustomerProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=str(self.id),
        )
        controller = deleteCustomerProfileController(request)
        self.execute_controller(controller)

    def _authorizenet_get_customer_profile(self, issuer_info: bool = True) -> dict:
        """Executes a :py:obj:`~authorizenet.apicontractsv1.getCustomerProfileRequest` using the Authorize.NET API."""
        assert self.id, "'id' was not set."
        request = getCustomerProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.id,
            includeIssuerInfo=str(issuer_info).lower(),
        )
        controller = getCustomerProfileController(request)
        response = self.execute_controller(controller)
        return response

    def _authorizenet_update_customer_profile(self, email: str, desc: str = "") -> None:
        """Executes an :py:obj:`~authorizenet.apicontractsv1.updateCustomerProfileRequest` using the Authorize.NET API."""
        assert self.id, "'id' was not set."
        request = updateCustomerProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            profile=customerProfileType(
                merchantCustomerId=self.merchantCustomerId,
                email=email,
                description=desc,
                customerProfileId=self.id,
            ),
        )
        controller = updateCustomerProfileController(request)
        self.execute_controller(controller)
