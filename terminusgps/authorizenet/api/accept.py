from authorizenet import apicontractsv1, apicontrollers
from authorizenet.apicontrollersbase import APIOperationBase
from lxml.objectify import ObjectifiedElement

__all__ = ["get_accept_customer_profile_page", "get_accept_payment_page"]


def get_accept_customer_profile_page(
    customer_profile_id: int, settings: apicontractsv1.ArrayOfSetting
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `getHostedProfilePageRequest <https://developer.authorize.net/api/reference/index.html#accept-suite-create-an-accept-payment-transaction>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: int
    :param settings: Hosted customer profile page settings.
    :type settings: ~authorizenet.apicontractsv1.ArrayOfSetting
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.getHostedProfilePageRequest()
    request.customerProfileId = customer_profile_id
    request.hostedProfileSettings = settings
    return request, apicontrollers.getHostedProfilePageController


def get_accept_payment_page(
    transaction_request: apicontractsv1.transactionRequestType,
    settings: apicontractsv1.ArrayOfSetting,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    """
    `getHostedPaymentPageRequest <https://developer.authorize.net/api/reference/index.html#accept-suite-get-an-accept-payment-page>`_.

    :param transaction_request: A transaction request.
    :type transaction_request: ~authorizenet.apicontractsv1.transactionRequestType
    :param settings: Hosted payment page settings.
    :type settings: ~authorizenet.apicontractsv1.ArrayOfSetting
    :returns: A tuple containing an Authorizenet API request element and controller class.
    :rtype: tuple[~lxml.objectify.ObjectifiedElement, type[~authorizenet.apicontrollersbase.APIOperationBase]]

    """
    request = apicontractsv1.getHostedPaymentPageRequest()
    request.transactionRequest = transaction_request
    request.hostedPaymentSettings = settings
    return request, apicontrollers.getHostedPaymentPageController
