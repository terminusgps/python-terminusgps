from authorizenet import apicontractsv1, apicontrollers

from terminusgps.authorizenet.auth import get_merchant_auth
from terminusgps.authorizenet.controllers import execute_controller


def create_customer_profile(merchant_id: int | str, email: str, description: str = ""):
    """
    `createCustomerProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-create-customer-profile>`_.

    :param merchant_id: A merchant designated customer id.
    :type merchant_id: :py:obj:`int` | :py:obj:`str`
    :param email: A customer email address.
    :type email: :py:obj:`str`
    :param description: An optional customer description.
    :type description: :py:obj:`str`
    :returns: An Authorizenet createCustomerProfile response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.createCustomerProfileRequest(
        merchantAuthentication=get_merchant_auth(),
        profile=apicontractsv1.customerProfileType(
            merchantCustomerId=str(merchant_id), description=description, email=email
        ),
    )
    return execute_controller(apicontrollers.createCustomerProfileController(request))


def get_customer_profile(customer_profile_id: int, include_issuer_info: bool = False):
    """
    `getCustomerProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-get-customer-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param include_issuer_info: Whether or not to include issuer info in the response. Default is :py:obj:`False`.
    :type include_issuer_info: :py:obj:`bool`
    :returns: An Authorizenet getCustomerProfile response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.getCustomerProfileRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        includeIssuerInfo=str(include_issuer_info).lower(),
    )
    return execute_controller(apicontrollers.getCustomerProfileController(request))


def get_customer_profile_ids():
    """
    `getCustomerProfileIdsRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-get-customer-profile-ids>`_.

    :returns: An Authorizenet getCustomerProfileIds response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.getCustomerProfileIdsRequest(
        merchantAuthentication=get_merchant_auth()
    )
    return execute_controller(apicontrollers.getCustomerProfileIdsController(request))


def update_customer_profile(
    customer_profile_id: int, new_profile: apicontractsv1.customerProfileExType
):
    """
    `updateCustomerProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-update-customer-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param new_profile: An Authorizenet customer profile ex object.
    :type new_profile: :py:obj:`~authorizenet.apicontractsv1.customerProfileExType`
    :returns: An Authorizenet updateCustomerProfile response.
    :rtype: :py:obj:`dict`

    """
    new_profile.customerProfileId = str(customer_profile_id)
    request = apicontractsv1.updateCustomerProfileRequest(
        merchantAuthentication=get_merchant_auth(), profile=new_profile
    )
    return execute_controller(apicontrollers.updateCustomerProfileController(request))


def delete_customer_profile(customer_profile_id: int):
    """
    `deleteCustomerProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-delete-customer-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :returns: An Authorizenet deleteCustomerProfile response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.deleteCustomerProfileRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
    )
    return execute_controller(apicontrollers.deleteCustomerProfileController(request))


def create_customer_shipping_address(
    customer_profile_id: int,
    new_address: apicontractsv1.customerAddressType,
    default: bool = True,
):
    """
    `createCustomerShippingAddressRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-create-customer-shipping-address>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param new_address: An Authorizenet customer address object.
    :type new_address: :py:obj:`~authorizenet.apicontractsv1.customerAddressType`
    :param default: Whether or not to mark the new shipping address as default. Default is :py:obj:`True`.
    :type default: :py:obj:`bool`
    :returns: An Authorizenet createCustomerShippingAddress response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.createCustomerShippingAddressRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        address=new_address,
        defaultShippingAddress=str(default).lower(),
    )
    return execute_controller(
        apicontrollers.createCustomerShippingAddressController(request)
    )


def get_customer_shipping_address(
    customer_profile_id: int, customer_address_profile_id: int
):
    """
    `getCustomerShippingAddressRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-get-customer-shipping-address>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param customer_address_profile_id: An Authorizenet customer address profile id.
    :type customer_address_profile_id: :py:obj:`int`
    :returns: An Authorizenet getCustomerShippingAddress response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.getCustomerShippingAddressRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        customerAddressId=str(customer_address_profile_id),
    )
    return execute_controller(
        apicontrollers.getCustomerShippingAddressController(request)
    )


def update_customer_shipping_address(
    customer_profile_id: int,
    new_address: apicontractsv1.customerAddressType,
    default: bool = False,
):
    """
    `updateCustomerShippingAddressRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-update-customer-shipping-address>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param new_address: An Authorizenet customer address object.
    :type new_address: :py:obj:`~authorizenet.apicontractsv1.customerAddressType`
    :param default: Whether or not to mark the new shipping address as default. Default is :py:obj:`False`.
    :type default: :py:obj:`bool`
    :returns: An Authorizenet updateCustomerShippingAddress response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.updateCustomerShippingAddressRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        address=new_address,
        defaultShippingAddress=str(default).lower(),
    )
    return execute_controller(
        apicontrollers.updateCustomerShippingAddressController(request)
    )


def delete_customer_shipping_address(
    customer_profile_id: int, customer_address_profile_id: int
):
    """
    `deleteCustomerShippingAddressRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-delete-customer-shipping-address>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param customer_address_profile_id: An Authorizenet customer address profile id.
    :type customer_address_profile_id: :py:obj:`int`
    :returns: An Authorizenet deleteCustomerShippingAddress response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.deleteCustomerShippingAddressRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        customerAddressId=str(customer_address_profile_id),
    )
    return execute_controller(
        apicontrollers.deleteCustomerShippingAddressController(request)
    )


def create_customer_payment_profile(
    customer_profile_id: int,
    new_payment_profile: apicontractsv1.customerPaymentProfileType,
):
    """
    `createCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-create-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param new_payment_profile: An Authorizenet payment profile object.
    :type new_payment_profile: :py:obj:`~authorizenet.apicontractsv1.customerPaymentProfileType`
    :returns: An Authorizenet createCustomerPaymentProfile response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.createCustomerPaymentProfileRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        paymentProfile=new_payment_profile,
        validationMode=get_validation_mode(),
    )
    return execute_controller(
        apicontrollers.createCustomerPaymentProfileController(request)
    )


def get_customer_payment_profile(
    customer_profile_id: int,
    customer_payment_profile_id: int,
    include_issuer_info: bool = False,
):
    """
    `getCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-get-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param customer_payment_profile_id: An Authorizenet customer payment profile id.
    :type customer_payment_profile_id: :py:obj:`int`
    :param include_issuer_info: Whether or not to include issuer info in the response. Default is :py:obj:`False`.
    :type include_issuer_info: :py:obj:`bool`
    :returns: An Authorizenet getCustomerPaymentProfile response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.getCustomerPaymentProfileRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        customerPaymentProfileId=str(customer_payment_profile_id),
        includeIssuerInfo=str(include_issuer_info).lower(),
    )
    return execute_controller(
        apicontrollers.getCustomerPaymentProfileController(request)
    )


def validate_customer_payment_profile(
    customer_profile_id: int, customer_payment_profile_id: int
):
    """
    `validateCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-validate-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param customer_payment_profile_id: An Authorizenet customer payment profile id.
    :type customer_payment_profile_id: :py:obj:`int`
    :returns: An Authorizenet validateCustomerPaymentProfile response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.validateCustomerPaymentProfileRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        customerPaymentProfileId=str(customer_payment_profile_id),
        validationMode=get_validation_mode(),
    )
    return execute_controller(
        apicontrollers.validateCustomerPaymentProfileController(request)
    )


def update_customer_payment_profile(
    customer_profile_id: int,
    customer_payment_profile_id: int,
    new_payment_profile: apicontractsv1.customerPaymentProfileType,
):
    """
    `updateCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-update-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param customer_payment_profile_id: An Authorizenet customer payment profile id.
    :type customer_payment_profile_id: :py:obj:`int`
    :param new_payment_profile: An Authorizenet payment profile object.
    :type new_payment_profile: :py:obj:`~authorizenet.apicontractsv1.customerPaymentProfileType`
    :returns: An Authorizenet updateCustomerPaymentProfile response.
    :rtype: :py:obj:`dict`

    """
    new_payment_profile.customerPaymentProfileId = str(customer_payment_profile_id)
    request = apicontractsv1.updateCustomerPaymentProfileRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        paymentProfile=new_payment_profile,
        validationMode=get_validation_mode(),
    )
    return execute_controller(
        apicontrollers.updateCustomerPaymentProfileController(request)
    )


def delete_customer_payment_profile(
    customer_profile_id: int, customer_payment_profile_id: int
):
    """
    `deleteCustomerPaymentProfileRequest <https://developer.authorize.net/api/reference/index.html#customer-profiles-delete-customer-payment-profile>`_.

    :param customer_profile_id: An Authorizenet customer profile id.
    :type customer_profile_id: :py:obj:`int`
    :param customer_payment_profile_id: An Authorizenet customer payment profile id.
    :type customer_payment_profile_id: :py:obj:`int`
    :returns: An Authorizenet deleteCustomerPaymentProfile response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.deleteCustomerPaymentProfileRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        customerPaymentProfileId=str(customer_payment_profile_id),
    )
    return execute_controller(
        apicontrollers.deleteCustomerPaymentProfileController(request)
    )


def create_subscription(subscription_obj: apicontractsv1.ARBSubscriptionType):
    """
    `ARBCreateSubscriptionRequest <https://developer.authorize.net/api/reference/index.html#recurring-billing-create-a-subscription>`_.

    :param subscription_obj: An Authorizenet subscription object.
    :type subscription_obj: :py:obj:`~authorizenet.apicontractsv1.ARBSubscriptionType`
    :returns: An Authorizenet ARBCreateSubscription response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.ARBCreateSubscriptionRequest(
        merchantAuthentication=get_merchant_auth(), subscription=subscription_obj
    )
    return execute_controller(apicontrollers.ARBCreateSubscriptionController(request))


def get_subscription(subscription_id: int, include_transactions: bool = True):
    """
    `ARBGetSubscriptionRequest <https://developer.authorize.net/api/reference/index.html#recurring-billing-get-subscription>`_.

    :param subscription_id: An Authorizenet subscription id.
    :type subscription_id: :py:obj:`int`
    :param include_transactions: Whether or not to include the subscription transaction list in the response. Default is :py:obj:`True`.
    :type include_transactions: :py:obj:`bool`
    :returns: An Authorizenet ARBGetSubscription response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.ARBGetSubscriptionRequest(
        merchantAuthentication=get_merchant_auth(),
        subscriptionId=str(subscription_id),
        includeTransactions=str(include_transactions).lower(),
    )
    return execute_controller(apicontrollers.ARBGetSubscriptionController(request))


def get_subscription_status(subscription_id: int):
    """
    `ARBGetSubscriptionStatusRequest <https://developer.authorize.net/api/reference/index.html#recurring-billing-get-subscription-status>`_.

    :param subscription_id: An Authorizenet subscription id.
    :type subscription_id: :py:obj:`int`
    :returns: An Authorizenet ARBGetSubscriptionStatus response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.ARBGetSubscriptionStatusRequest(
        merchantAuthentication=get_merchant_auth(), subscriptionId=str(subscription_id)
    )
    return execute_controller(
        apicontrollers.ARBGetSubscriptionStatusController(request)
    )


def update_subscription(
    subscription_id: int, subscription_obj: apicontractsv1.ARBSubscriptionType
):
    """
    `ARBUpdateSubscriptionRequest <https://developer.authorize.net/api/reference/index.html#recurring-billing-update-a-subscription>`_.

    :param subscription_id: An Authorizenet subscription id.
    :type subscription_id: :py:obj:`int`
    :param subscription_obj: An Authorizenet subscription object.
    :type subscription_obj: :py:obj:`~authorizenet.apicontractsv1.ARBSubscriptionType`
    :returns: An Authorizenet ARBUpdateSubscription response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.ARBUpdateSubscriptionRequest(
        merchantAuthentication=get_merchant_auth(),
        subscriptionId=str(subscription_id),
        subscription=subscription_obj,
    )
    return execute_controller(apicontrollers.ARBUpdateSubscriptionController(request))


def cancel_subscription(subscription_id: int):
    """
    `ARBCancelSubscriptionRequest <https://developer.authorize.net/api/reference/index.html#recurring-billing-cancel-a-subscription>`_.

    :param subscription_id: An Authorizenet subscription id.
    :type subscription_id: :py:obj:`int`
    :returns: An Authorizenet ARBCancelSubscription response.
    :rtype: :py:obj:`dict`

    """
    request = apicontractsv1.ARBCancelSubscriptionRequest(
        merchantAuthentication=get_merchant_auth(), subscriptionId=str(subscription_id)
    )
    return execute_controller(apicontrollers.ARBCancelSubscriptionController(request))
