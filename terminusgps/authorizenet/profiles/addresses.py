from authorizenet.apicontractsv1 import (
    createCustomerShippingAddressRequest,
    customerAddressType,
    deleteCustomerShippingAddressRequest,
    updateCustomerShippingAddressRequest,
    getCustomerShippingAddressRequest,
    getCustomerShippingAddressResponse,
)
from authorizenet.apicontrollers import (
    createCustomerShippingAddressController,
    deleteCustomerShippingAddressController,
    getCustomerShippingAddressController,
    updateCustomerShippingAddressController,
)
from terminusgps.authorizenet.profiles.base import AuthorizenetCustomerProfileBase


class AddressProfile(AuthorizenetCustomerProfileBase):
    def create(self, **kwargs) -> int:
        if not kwargs.get("address"):
            raise ValueError("'address' is required on creation.")

        request = createCustomerShippingAddressRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            address=kwargs["address"],
            defaultShippingAddress=self.default,
        )
        controller = createCustomerShippingAddressController(request)
        response = self.execute_controller(controller)
        return int(response.get("customerAddressId"))

    def delete(self) -> None:
        request = deleteCustomerShippingAddressRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerAddressId=self.id,
        )
        controller = deleteCustomerShippingAddressController(request)
        self.execute_controller(controller)

    def update(self, address: customerAddressType, default: bool = False) -> None:
        request = updateCustomerShippingAddressRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            address=address,
            defaultShippingAddress=default,
        )
        controller = updateCustomerShippingAddressController(request)
        self.execute_controller(controller)
        self._default = default

    def get_details(self) -> getCustomerShippingAddressResponse:
        request = getCustomerShippingAddressRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerAddressId=self.id,
        )
        controller = getCustomerShippingAddressController(request)
        return self.execute_controller(controller)
