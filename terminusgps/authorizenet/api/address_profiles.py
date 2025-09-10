from authorizenet import apicontractsv1, apicontrollers
from authorizenet.apicontrollersbase import APIOperationBase
from lxml.objectify import ObjectifiedElement

__all__ = [
    "create_customer_shipping_address",
    "get_customer_shipping_address",
    "update_customer_shipping_address",
    "delete_customer_shipping_address",
]


def create_customer_shipping_address(
    customer_profile_id: int,
    address: apicontractsv1.customerAddressType,
    default: bool = False,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `createCustomerShippingAddressRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-create-customer-shipping-address>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param address: An Authorizenet customer address element.
    :type address: ~authorizenet.apicontractsv1.customerAddressType
    :param default: Whether to set the address profile as default. Default is :py:obj:`False`.
    :type default: bool
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.createCustomerShippingAddressRequest()
    request.customerProfileId = str(customer_profile_id)
    request.address = address
    request.defaultShippingAddress = str(default).lower()
    return request, apicontrollers.createCustomerShippingAddressController


def get_customer_shipping_address(
    customer_profile_id: int, address_profile_id: int
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `getCustomerShippingAddressRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-get-customer-shipping-address>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param address_profile_id: An Authorizenet customer address profile id.
    :type address_profile_id: int
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.getCustomerShippingAddressRequest()
    request.customerProfileId = str(customer_profile_id)
    request.customerAddressId = str(address_profile_id)
    return request, apicontrollers.getCustomerShippingAddressController


def update_customer_shipping_address(
    customer_profile_id: int,
    address: apicontractsv1.customerAddressType,
    default: bool = False,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `updateCustomerShippingAddressRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-update-customer-shipping-address>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param address: An Authorizenet customer address element.
    :type address: ~authorizenet.apicontractsv1.customerAddressType
    :param default: Whether to set the address profile as default. Default is :py:obj:`False`.
    :type default: bool
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.updateCustomerShippingAddressRequest()
    request.customerProfileId = str(customer_profile_id)
    request.address = address
    request.defaultShippingAddress = str(default).lower()
    return request, apicontrollers.updateCustomerShippingAddressController


def delete_customer_shipping_address(
    customer_profile_id: int, address_profile_id: int
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `deleteCustomerShippingAddressRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-delete-customer-shipping-address>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param address_profile_id: An Authorizenet customer address profile id.
    :type address_profile_id: int
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.deleteCustomerShippingAddressRequest()
    request.customerProfileId = str(customer_profile_id)
    request.customerAddressId = str(address_profile_id)
    return request, apicontrollers.deleteCustomerShippingAddressController
