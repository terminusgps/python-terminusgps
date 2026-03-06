from authorizenet import apicontractsv1, apicontrollers
from authorizenet.apicontrollersbase import APIOperationBase
from lxml.objectify import ObjectifiedElement

__all__ = [
    "create_customer_payment_profile",
    "get_customer_payment_profile",
    "validate_customer_payment_profile",
    "update_customer_payment_profile",
    "delete_customer_payment_profile",
]


def create_customer_payment_profile(
    customer_profile_id: int,
    contract: apicontractsv1.customerPaymentProfileType,
    default: bool = False,
    validation: str = "liveMode",
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `createCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-create-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param contract: A customer payment profile element.
    :type contract: ~authorizenet.apicontractsv1.customerPaymentProfileType
    :param default: Whether to set the payment profile as default. Default is :py:obj:`False`.
    :type default: bool
    :param validation: Validation mode. Default is :py:obj:`"liveMode"`.
    :type validation: str
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    if not contract.payment:
        raise ValueError("'payment' attribute is required in contract")
    if not contract.billTo:
        raise ValueError("'billTo' attribute is required in contract")
    request = apicontractsv1.createCustomerPaymentProfileRequest()
    request.customerProfileId = str(customer_profile_id)
    request.validationMode = validation
    request.paymentProfile = contract
    request.paymentProfile.defaultPaymentProfile = int(default)
    return request, apicontrollers.createCustomerPaymentProfileController


def get_customer_payment_profile(
    customer_profile_id: int,
    payment_profile_id: int,
    include_issuer_info: bool = False,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `getCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-get-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param payment_profile_id: An Authorizenet customer payment profile id.
    :type payment_profile_id: int
    :param include_issuer_info: Whether to include issuer info in the response. Default is False.
    :type include_issuer_info: bool
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.getCustomerPaymentProfileRequest()
    request.customerProfileId = str(customer_profile_id)
    request.customerPaymentProfileId = str(payment_profile_id)
    request.includeIssuerInfo = int(include_issuer_info)
    return request, apicontrollers.getCustomerPaymentProfileController


def validate_customer_payment_profile(
    customer_profile_id: int,
    payment_profile_id: int,
    validation: str = "liveMode",
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `validateCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-validate-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param payment_profile_id: An Authorizenet customer payment profile id.
    :type payment_profile_id: int
    :param validation: Validation mode. Default is :py:obj:`"liveMode"`.
    :type validation: str
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.validateCustomerPaymentProfileRequest()
    request.customerProfileId = str(customer_profile_id)
    request.customerPaymentProfileId = str(payment_profile_id)
    request.validationMode = validation
    return request, apicontrollers.validateCustomerPaymentProfileController


def update_customer_payment_profile(
    customer_profile_id: int,
    contract: apicontractsv1.customerPaymentProfileExType,
    default: bool,
    validation: str = "liveMode",
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `updateCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-update-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param contract: A customer payment profile ex element.
    :type contract: ~authorizenet.apicontractsv1.customerPaymentProfileExType
    :param default: Whether to set the payment profile as default.
    :type default: bool
    :param validation: Validation mode. Default is :py:obj:`"liveMode"`.
    :type validation: str
    :raises ValueError: If neither payment nor address was provided.
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    if not contract.payment:
        raise ValueError("'payment' attribute is required in contract")
    if not contract.billTo:
        raise ValueError("'billTo' attribute is required in contract")
    if not contract.customerPaymentProfileId:
        raise ValueError("'customerPaymentProfileId' is required in contract")
    request = apicontractsv1.updateCustomerPaymentProfileRequest()
    request.customerProfileId = str(customer_profile_id)
    request.validationMode = validation
    request.paymentProfile = contract
    request.paymentProfile.defaultPaymentProfile = int(default)
    return request, apicontrollers.updateCustomerPaymentProfileController


def delete_customer_payment_profile(
    customer_profile_id: int, payment_profile_id: int
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `deleteCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-delete-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param payment_profile_id: An Authorizenet customer payment profile id.
    :type payment_profile_id: int
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.deleteCustomerPaymentProfileRequest()
    request.customerProfileId = str(customer_profile_id)
    request.customerPaymentProfileId = str(payment_profile_id)
    return request, apicontrollers.deleteCustomerPaymentProfileController
