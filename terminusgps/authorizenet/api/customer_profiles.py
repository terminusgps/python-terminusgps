from authorizenet import apicontractsv1, apicontrollers
from authorizenet.apicontrollersbase import APIOperationBase
from lxml.objectify import ObjectifiedElement

__all__ = [
    "create_customer_profile",
    "delete_customer_profile",
    "get_customer_profile",
    "get_customer_profile_ids",
    "update_customer_profile",
]


def create_customer_profile(
    contract: apicontractsv1.customerProfileType,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `createCustomerProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-create-customer-profile>`_.

    :param contract: A customer profile contract element.
    :type contract: ~apicontractsv1.customerProfileType
    :raises ValueError: If the contract didn't have at least one of ``email``, ``merchantCustomerId`` or ``description``.
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    if not any(
        [contract.email, contract.merchantCustomerId, contract.description]
    ):
        raise ValueError(
            "At least one of 'email', 'merchantCustomerId' or 'description' is required in contract"
        )

    request = apicontractsv1.createCustomerProfileRequest()
    request.profile = contract
    return request, apicontrollers.createCustomerProfileController


def get_customer_profile(
    customer_profile_id: int | None = None,
    email: str | None = None,
    merchant_id: str | None = None,
    description: str | None = None,
    include_issuer_info: bool = False,
    unmask_expiration_date: bool = False,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `getCustomerProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-get-customer-profile>`_.

    :param customer_profile_id: Authorizenet customer profile id.
    :type customer_profile_id: int | None
    :param email: Authorizenet customer profile email.
    :type email: str | None
    :param merchant_id: Authorizenet customer profile merchant id.
    :type merchant_id: str | None
    :param description: Authorizenet customer profile description.
    :type description: str | None
    :param include_issuer_info: Whether to include issuer info in the response. Default is :py:obj:`False`.
    :type include_issuer_info: bool
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    if not any([customer_profile_id, email, merchant_id, description]):
        raise ValueError(
            "At least one of 'customer_profile_id', 'email', 'merchant_id' or 'description' is required."
        )

    request = apicontractsv1.getCustomerProfileRequest()
    request.includeIssuerInfo = str(include_issuer_info).lower()
    request.unmaskExpirationDate = str(unmask_expiration_date).lower()
    if customer_profile_id is not None:
        request.customerProfileId = str(customer_profile_id)
    if email is not None:
        request.email = email
    if merchant_id is not None:
        request.merchantCustomerId = merchant_id
    if description is not None:
        request.description = description
    return request, apicontrollers.getCustomerProfileController


def get_customer_profile_ids() -> tuple[
    ObjectifiedElement, type[APIOperationBase]
]:
    """
    `getCustomerProfileIdsRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-get-customer-profile-ids>`_.

    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.getCustomerProfileIdsRequest()
    return request, apicontrollers.getCustomerProfileIdsController


def update_customer_profile(
    contract: apicontractsv1.customerProfileExType,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `updateCustomerProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-update-customer-profile>`_.

    :param contract: An Authorizenet customer profile ex contract.
    :type contract: ~authorizenet.apicontractsv1.customerProfileExType
    :raises TypeError: If the contract wasn't of type :py:class:`~apicontractsv1.customerProfileExType`.
    :raises ValueError: If the contract didn't have all required attributes.
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    if not contract.customerProfileId:
        raise ValueError(
            f"Invalid value for 'customerProfileId': '{contract.customerProfileId}'"
        )
    request = apicontractsv1.updateCustomerProfileRequest()
    request.profile = contract
    return request, apicontrollers.updateCustomerProfileController


def delete_customer_profile(
    customer_profile_id: int,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `deleteCustomerProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-delete-customer-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.deleteCustomerProfileRequest()
    request.customerProfileId = str(customer_profile_id)
    return request, apicontrollers.deleteCustomerProfileController
