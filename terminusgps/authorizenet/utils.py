from authorizenet import apicontractsv1, apicontrollers
from django import forms

from .auth import get_merchant_auth
from .controllers import AuthorizenetControllerExecutor


def get_payment_profile_transactions(
    customer_profile_id: int | str,
    payment_profile_id: int | str,
    descending: bool = False,
    limit: int = 100,
    offset: int = 0,
) -> dict | None:
    """
    Returns a transaction list for a customer payment profile.

    `getTransactionListForCustomerRequest <https://developer.authorize.net/api/reference/index.html#transaction-reporting-get-customer-profile-transaction-list>`_

    :param customer_profile_id: A customer profile id.
    :type customer_profile_id: :py:obj:`int` | :py:obj:`str`
    :param payment_profile_id: A customer payment profile id.
    :type payment_profile_id: :py:obj:`int` | :py:obj:`str`
    :param descending: Whether or not to sort the response in descending order. Default is :py:obj:`False`.
    :type descending: :py:obj:`bool`
    :param limit: Maximum amount of transactions to return in the response. Default is :py:obj:`100` .
    :type limit: :py:obj:`int`
    :param offset: Offsets the response for pagination. Default is :py:obj:`0` for page 0.
    :type offset: :py:obj:`int`
    :raises ValueError: If ``customer_profile_id`` was provided as a string containing non-digits.
    :raises ValueError: If ``payment_profile_id`` was provided as a string containing non-digits.
    :raises AuthorizenetControllerExecutionError: If the API call fails.
    :returns: A merchant details object, if found.
    :rtype: :py:obj:`dict` | :py:obj:`None`

    """
    raise NotImplementedError

    if isinstance(customer_profile_id, str) and not customer_profile_id.isdigit():
        raise ValueError(
            f"'customer_profile_id' can only contain digits, got '{customer_profile_id}'."
        )
    if isinstance(payment_profile_id, str) and not payment_profile_id.isdigit():
        raise ValueError(
            f"'payment_profile_id' can only contain digits, got '{payment_profile_id}'."
        )

    request = apicontractsv1.getTransactionListForCustomerRequest(
        merchantAuthentication=get_merchant_auth(),
        customerProfileId=str(customer_profile_id),
        customerPaymentProfileId=str(payment_profile_id),
        sorting={
            "orderBy": "submitTimeUTC",
            "orderDescending": str(descending).lower(),
        },
        paging={"limit": limit, "offset": offset},
    )
    controller = apicontrollers.getTransactionListForCustomerController(request)
    return AuthorizenetControllerExecutor.execute_controller(controller)


def get_merchant_details() -> dict | None:
    """
    Returns Authorizenet merchant details.

    `getMerchantDetailsRequest <http://developer.authorize.net/api/reference/index.html#transaction-reporting-get-merchant-details>`_

    :raises AuthorizenetControllerExecutionError: If the API call fails.
    :returns: A merchant details object, if found.
    :rtype: :py:obj:`dict` | :py:obj:`None`

    """
    request = apicontractsv1.getMerchantDetailsRequest(
        merchantAuthentication=get_merchant_auth()
    )
    controller = apicontrollers.getMerchantDetailsController(request)
    return AuthorizenetControllerExecutor.execute_controller(controller)


def get_transaction(id: int | str) -> dict | None:
    """
    Returns Authorizenet transaction details by id.

    `getTransactionDetailsRequest <https://developer.authorize.net/api/reference/index.html#transaction-reporting-get-transaction-details>`_

    :param id: An Authorizenet transaction id.
    :type id: :py:obj:`int` | :py:obj:`str`
    :raises ValueError: If ``id`` was provided as a string containing non-digits.
    :raises AuthorizenetControllerExecutionError: If the API call fails.
    :returns: A transaction object, if found.
    :rtype: :py:obj:`dict` | :py:obj:`None`

    """
    if isinstance(id, str) and not id.isdigit():
        raise ValueError(f"'id' can only contain digits, got '{id}'.")

    request = apicontractsv1.getTransactionDetailsRequest(
        merchantAuthentication=get_merchant_auth(), transId=str(id)
    )
    controller = apicontrollers.getTransactionDetailsController(request)
    return AuthorizenetControllerExecutor.execute_controller(controller)


def get_customer_profile_ids() -> list[int]:
    """
    Returns a list of all customer profile ids in Authorizenet.

    :raises AuthorizenetControllerExecutionError: If the API call fails.
    :returns: A list of all customer profile ids in Authorizenet.
    :rtype: :py:obj:`list`

    """
    request = apicontractsv1.getCustomerProfileIdsRequest(
        merchantAuthentication=get_merchant_auth()
    )
    controller = apicontrollers.getCustomerProfileIdsController(request)
    response = AuthorizenetControllerExecutor.execute_controller(controller)
    if response is None or "ids" not in response.getchildren():
        return []
    return [int(id) for id in response.ids.getchildren()]


def generate_customer_address(form: forms.Form) -> apicontractsv1.customerAddressType:
    """
    Takes a form and returns a :py:obj:`~authorizenet.apicontractsv1.customerAddressType`.

    Required form fields:

    +----------------+------------------------------------------------------------+
    | name           | type                                                       |
    +================+============================================================+
    | ``address``    | :py:obj:`~authorizenet.apicontractsv1.customerAddressType` |
    +----------------+------------------------------------------------------------+
    | ``first_name`` | :py:obj:`str`                                              |
    +----------------+------------------------------------------------------------+
    | ``last_name``  | :py:obj:`str`                                              |
    +----------------+------------------------------------------------------------+

    :param form: A Django form.
    :type form: :py:obj:`~django.forms.Form`
    :raises ValueError: If ``address`` wasn't in the form.
    :raises ValueError: If ``first_name`` wasn't in the form.
    :raises ValueError: If ``last_name`` wasn't in the form.
    :returns: A customer address object.
    :rtype: :py:obj:`~authorizenet.apicontractsv1.customerAddressType`

    """
    required_fields: list[str] = ["address", "first_name", "last_name"]
    for field in required_fields:
        if field not in form.cleaned_data or form.cleaned_data.get(field) is None:
            raise ValueError(
                f"'{field}' was not provided by the form, got '{form.cleaned_data.get(field)}'."
            )

    address: apicontractsv1.customerAddressType = form.cleaned_data["address"]
    address.firstName = form.cleaned_data["first_name"]
    address.lastName = form.cleaned_data["last_name"]
    if form.cleaned_data.get("phone"):
        address.phone = form.cleaned_data["phone"]
    return address


def generate_customer_payment(form: forms.Form) -> apicontractsv1.paymentType:
    """
    Takes a form and returns a :py:obj:`~authorizenet.apicontractsv1.paymentType`.

    Required form fields:

    +-----------------+-------------------------------------------------------+
    | name            | type                                                  |
    +=================+=======================================================+
    | ``credit_card`` | :py:obj:`~authorizenet.apicontractsv1.creditCardType` |
    +-----------------+-------------------------------------------------------+

    :param form: A Django form.
    :type form: :py:obj:`~django.forms.Form`
    :raises ValueError: If ``credit_card`` wasn't in the form.
    :returns: A payment object.
    :rtype: :py:obj:`~authorizenet.apicontractsv1.paymentType`

    """
    required_fields: list[str] = ["credit_card"]
    for field in required_fields:
        if field not in form.cleaned_data or form.cleaned_data.get(field) is None:
            raise ValueError(
                f"'{field}' was not provided by the form, got '{form.cleaned_data.get(field)}'."
            )

    credit_card: apicontractsv1.creditCardType = form.cleaned_data["credit_card"]
    return apicontractsv1.paymentType(creditCard=credit_card)
