from decimal import Decimal

from authorizenet import apicontractsv1, apicontrollers
from authorizenet.apicontrollersbase import APIOperationBase
from lxml.objectify import ObjectifiedElement

__all__ = []


def build_transaction_request(
    transaction_type: str,
    amount: Decimal,
    payment: apicontractsv1.paymentType | None = None,
    order: apicontractsv1.orderType | None = None,
    address: apicontractsv1.customerAddressType | None = None,
    customer_data: apicontractsv1.customerDataType | None = None,
    settings: apicontractsv1.settingType | None = None,
    line_items: apicontractsv1.ArrayOfLineItem | None = None,
) -> apicontractsv1.transactionRequestType:
    request = apicontractsv1.transactionRequestType()
    request.transactionType = transaction_type
    request.amount = amount

    if payment is not None:
        request.payment = payment
    if order is not None:
        request.order = order
    if address is not None:
        request.billTo = address
    if customer_data is not None:
        request.customer = customer_data
    if settings is not None:
        request.transactionSettings = settings
    if line_items is not None:
        request.lineItems = line_items
    return request


def charge_credit_card(
    amount: Decimal,
    credit_card: apicontractsv1.creditCardType,
    address: apicontractsv1.customerAddressType,
    order: apicontractsv1.orderType | None = None,
    customer_data: apicontractsv1.customerDataType | None = None,
    settings: apicontractsv1.settingType | None = None,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    request = apicontractsv1.createTransactionRequest()
    request.transactionRequest = build_transaction_request(
        transaction_type="authCaptureTransaction",
        amount=amount,
        payment=apicontractsv1.paymentType(creditCard=credit_card),
        address=address,
        order=order,
        customer_data=customer_data,
        settings=settings,
    )
    return request, apicontrollers.createTransactionController


def authorize_credit_card(
    amount: Decimal,
    credit_card: apicontractsv1.creditCardType,
    address: apicontractsv1.customerAddressType,
    order: apicontractsv1.orderType | None = None,
    customer_data: apicontractsv1.customerDataType | None = None,
    settings: apicontractsv1.settingType | None = None,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    request = apicontractsv1.createTransactionRequest()
    request.transactionRequest = build_transaction_request(
        transaction_type="authOnlyTransaction",
        amount=amount,
        payment=apicontractsv1.paymentType(creditCard=credit_card),
        address=address,
        order=order,
        customer_data=customer_data,
        settings=settings,
    )
    return request, apicontrollers.createTransactionController


def capture_authorized_amount(
    amount: Decimal,
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    request = apicontractsv1.createTransactionRequest()
    request.transactionRequest = build_transaction_request(
        transaction_type="priorAuthCaptureTransaction", amount=amount
    )
    return request, apicontrollers.createTransactionController


def refund_credit_card(
    amount: Decimal, credit_card: apicontractsv1.creditCardType
) -> tuple[ObjectifiedElement, type[APIOperationBase]]:
    request = apicontractsv1.createTransactionRequest()
    request.transactionRequest = build_transaction_request(
        transaction_type="refundTransaction",
        amount=amount,
        payment=apicontractsv1.paymentType(creditCard=credit_card),
    )
    return request, apicontrollers.createTransactionController
