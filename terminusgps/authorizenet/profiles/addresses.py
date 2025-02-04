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
        shipping_addr = kwargs.get("shipping_addr")

        if not shipping_addr:
            raise ValueError("'shipping_addr' is required on creation.")

        if not isinstance(shipping_addr, customerAddressType):
            raise TypeError(
                f"'shipping_addr' must be customerAddressType, got '{type(shipping_addr)}'."
            )

        return self._authorizenet_create_shipping_address(shipping_addr)

    def delete(self) -> None:
        self._authorizenet_delete_shipping_address()

    def update(self, shipping_addr: customerAddressType) -> None:
        self._authorizenet_update_shipping_address(shipping_addr)

    def get_details(self) -> dict:
        return self._authorizenet_get_shipping_address()

    def _authorizenet_create_shipping_address(self, addr: customerAddressType) -> int:
        request = createCustomerShippingAddressRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            address=addr,
            defaultShippingAddress=self.default,
        )
        controller = createCustomerShippingAddressController(request)
        response = self.execute_controller(controller)
        return int(response.customerAddressId)

    def _authorizenet_update_shipping_address(self, addr: customerAddressType) -> None:
        assert self.id, "'id' was not set."
        addr.customerAddressId = self.id
        request = updateCustomerShippingAddressRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            address=addr,
            default=self.default,
        )
        controller = updateCustomerShippingAddressController(request)
        self.execute_controller(controller)

    def _authorizenet_get_shipping_address(self) -> dict:
        assert self.id, "'id' was not set."
        request = getCustomerShippingAddressRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerAddressId=self.id,
        )
        controller = getCustomerShippingAddressController(request)
        response = self.execute_controller(controller)
        return response

    def _authorizenet_delete_shipping_address(self) -> None:
        assert self.id, "'id' was not set."
        request = deleteCustomerShippingAddressRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.customerProfileId,
            customerAddressId=self.id,
        )
        controller = deleteCustomerShippingAddressController(request)
        self.execute_controller(controller)
