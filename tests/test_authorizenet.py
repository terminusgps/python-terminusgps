import unittest

from authorizenet import apicontractsv1, apicontrollers

from terminusgps.authorizenet import api


class CreateCustomerShippingAddressFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.create_customer_shipping_address

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {
            "customer_profile_id": 1,
            "contract": apicontractsv1.customerAddressType(),
            "default": False,
        }
        expected = apicontrollers.createCustomerShippingAddressController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "customer_profile_id": 1,
            "contract": apicontractsv1.customerAddressType(),
            "default": False,
        }
        request, _ = self.func(**kwargs)
        self.assertEqual(request.address, kwargs["contract"])
        self.assertEqual(
            request.defaultShippingAddress, int(kwargs["default"])
        )
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )


class GetCustomerShippingAddressFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.get_customer_shipping_address

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {"customer_profile_id": 1, "address_profile_id": 1}
        expected = apicontrollers.getCustomerShippingAddressController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {"customer_profile_id": 1, "address_profile_id": 1}
        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )
        self.assertEqual(
            request.customerAddressId, str(kwargs["address_profile_id"])
        )


class UpdateCustomerShippingAddressFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.update_customer_shipping_address

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {
            "customer_profile_id": 1,
            "contract": apicontractsv1.customerAddressExType(
                customerAddressId="1"
            ),
            "default": False,
        }
        expected = apicontrollers.updateCustomerShippingAddressController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_invalid_contract_values_raises_valueerror(self):
        """Fails if :py:exec:`ValueError` wasn't raised when calling the function with a contract with invalid values."""
        kwargs = {
            "customer_profile_id": 1,
            "contract": apicontractsv1.customerAddressExType(
                customerAddressId=None
            ),
            "default": False,
        }
        with self.assertRaises(ValueError):
            self.func(**kwargs)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "customer_profile_id": 1,
            "contract": apicontractsv1.customerAddressExType(
                customerAddressId="1"
            ),
            "default": False,
        }

        request, _ = self.func(**kwargs)
        self.assertEqual(request.address, kwargs["contract"])
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )
        self.assertEqual(
            request.defaultShippingAddress, int(kwargs["default"])
        )


class DeleteCustomerShippingAddressFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.delete_customer_shipping_address

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {"customer_profile_id": 1, "address_profile_id": 1}
        expected = apicontrollers.deleteCustomerShippingAddressController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {"customer_profile_id": 1, "address_profile_id": 1}
        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )
        self.assertEqual(
            request.customerAddressId, str(kwargs["address_profile_id"])
        )


class CreateCustomerProfileFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.create_customer_profile

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {
            "contract": apicontractsv1.customerProfileType(
                email="testuser@domain.com",
                merchantCustomerId="Test User",
                description="Test Description",
            )
        }
        expected = apicontrollers.createCustomerProfileController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_invalid_contract_values_raises_valueerror(self):
        """Fails if :py:exec:`ValueError` wasn't raised when calling the function with a contract with invalid values."""
        kwargs = {
            "contract": apicontractsv1.customerProfileType(
                email=None, merchantCustomerId=None, description=None
            )
        }
        with self.assertRaises(ValueError):
            self.func(**kwargs)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "contract": apicontractsv1.customerProfileType(
                email="testuser@domain.com",
                merchantCustomerId="Test User",
                description="Test Description",
            )
        }
        request, _ = self.func(**kwargs)
        self.assertEqual(request.profile, kwargs["contract"])


class GetCustomerProfileFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.get_customer_profile

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {
            "customer_profile_id": 1,
            "email": "testuser@domain.com",
            "merchant_id": "Test Merchant ID",
            "description": "Test Description",
            "include_issuer_info": False,
            "unmask_expiration_date": False,
        }
        expected = apicontrollers.getCustomerProfileController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_invalid_args_raises_valueerror(self):
        """Fails if :py:exec:`ValueError` wasn't raised when calling the function without providing required arguments."""
        kwargs = {
            "customer_profile_id": None,
            "email": None,
            "merchant_id": None,
            "description": None,
            "include_issuer_info": False,
            "unmask_expiration_date": False,
        }
        with self.assertRaises(ValueError):
            self.func(**kwargs)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "customer_profile_id": 1,
            "email": "testuser@domain.com",
            "merchant_id": "Test Merchant ID",
            "description": "Test Description",
            "include_issuer_info": True,
            "unmask_expiration_date": True,
        }

        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )
        self.assertEqual(request.email, kwargs["email"])
        self.assertEqual(request.merchantCustomerId, kwargs["merchant_id"])
        self.assertEqual(request.description, kwargs["description"])
        self.assertEqual(
            request.includeIssuerInfo, int(kwargs["include_issuer_info"])
        )
        self.assertEqual(
            request.unmaskExpirationDate, int(kwargs["unmask_expiration_date"])
        )


class GetCustomerProfileIdsFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.get_customer_profile_ids

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        expected = apicontrollers.getCustomerProfileIdsController
        _, controller = self.func()
        self.assertIs(controller, expected)


class UpdateCustomerProfileFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.update_customer_profile

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {
            "contract": apicontractsv1.customerProfileExType(
                customerProfileId="1",
                merchantCustomerId="Test Merchant ID",
                email="testuser@domain.com",
                description="Test Description",
            )
        }
        expected = apicontrollers.updateCustomerProfileController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_invalid_contract_values_raises_valueerror(self):
        """Fails if :py:exec:`ValueError` wasn't raised when calling the function with a contract with invalid values."""
        kwargs = {
            "contract": apicontractsv1.customerProfileExType(
                customerProfileId=None,
                merchantCustomerId="Test Merchant ID",
                email="testuser@domain.com",
                description="Test Description",
            )
        }
        with self.assertRaises(ValueError):
            self.func(**kwargs)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "contract": apicontractsv1.customerProfileExType(
                customerProfileId="1",
                merchantCustomerId="Test Merchant ID",
                email="testuser@domain.com",
                description="Test Description",
            )
        }
        request, _ = self.func(**kwargs)
        self.assertEqual(request.profile, kwargs["contract"])


class DeleteCustomerProfileFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.delete_customer_profile

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {"customer_profile_id": 1}
        expected = apicontrollers.deleteCustomerProfileController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {"customer_profile_id": 1}
        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )


class CreateCustomerPaymentProfileFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.create_customer_payment_profile

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {
            "customer_profile_id": 1,
            "contract": apicontractsv1.customerPaymentProfileType(
                billTo=apicontractsv1.customerAddressType(),
                payment=apicontractsv1.paymentType(),
                defaultPaymentProfile="1",
            ),
            "validation": "testMode",
        }
        expected = apicontrollers.createCustomerPaymentProfileController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_invalid_contract_values_raises_valueerror(self):
        """Fails if :py:exec:`ValueError` wasn't raised when calling the function with a contract with invalid values."""
        with self.assertRaises(ValueError):
            kwargs = {
                "customer_profile_id": 1,
                "contract": apicontractsv1.customerPaymentProfileType(
                    billTo=None,
                    payment=apicontractsv1.paymentType(),
                    defaultPaymentProfile="1",
                ),
                "validation": "testMode",
            }
            self.func(**kwargs)
        with self.assertRaises(ValueError):
            kwargs = {
                "customer_profile_id": 1,
                "contract": apicontractsv1.customerPaymentProfileType(
                    billTo=apicontractsv1.customerAddressType(),
                    payment=None,
                    defaultPaymentProfile="1",
                ),
                "validation": "testMode",
            }
            self.func(**kwargs)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "customer_profile_id": 1,
            "contract": apicontractsv1.customerPaymentProfileType(
                billTo=apicontractsv1.customerAddressType(),
                payment=apicontractsv1.paymentType(),
                defaultPaymentProfile="1",
            ),
            "validation": "testMode",
        }

        request, _ = self.func(**kwargs)
        self.assertEqual(request.paymentProfile, kwargs["contract"])
        self.assertEqual(request.validationMode, kwargs["validation"])
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )
        self.assertEqual(request.paymentProfile.defaultPaymentProfile, 1)


class GetCustomerPaymentProfileFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.get_customer_payment_profile

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {
            "customer_profile_id": 1,
            "payment_profile_id": 1,
            "include_issuer_info": False,
        }
        expected = apicontrollers.getCustomerPaymentProfileController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "customer_profile_id": 1,
            "payment_profile_id": 1,
            "include_issuer_info": True,
        }

        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )
        self.assertEqual(
            request.includeIssuerInfo, int(kwargs["include_issuer_info"])
        )
        self.assertEqual(
            request.customerPaymentProfileId, str(kwargs["payment_profile_id"])
        )


class ValidateCustomerPaymentProfileFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.validate_customer_payment_profile

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        expected = apicontrollers.validateCustomerPaymentProfileController
        kwargs = {
            "customer_profile_id": 1,
            "payment_profile_id": 1,
            "validation": "testMode",
        }
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "customer_profile_id": 1,
            "payment_profile_id": 1,
            "validation": "testMode",
        }
        request, _ = self.func(**kwargs)
        self.assertEqual(request.validationMode, kwargs["validation"])
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )
        self.assertEqual(
            request.customerPaymentProfileId, str(kwargs["payment_profile_id"])
        )


class UpdateCustomerPaymentProfileFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.update_customer_payment_profile

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {
            "customer_profile_id": 1,
            "contract": apicontractsv1.customerPaymentProfileExType(
                payment=apicontractsv1.paymentType(),
                billTo=apicontractsv1.customerAddressType(),
                customerPaymentProfileId="1",
                defaultPaymentProfile="1",
            ),
            "validation": "testMode",
        }
        expected = apicontrollers.updateCustomerPaymentProfileController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "customer_profile_id": 1,
            "contract": apicontractsv1.customerPaymentProfileExType(
                payment=apicontractsv1.paymentType(),
                billTo=apicontractsv1.customerAddressType(),
                customerPaymentProfileId="1",
                defaultPaymentProfile="1",
            ),
            "validation": "testMode",
        }

        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )
        self.assertEqual(request.paymentProfile, kwargs["contract"])
        self.assertEqual(request.validationMode, kwargs["validation"])
        self.assertEqual(request.paymentProfile.defaultPaymentProfile, 1)

    def test_invalid_contract_values_raises_valueerror(self):
        """Fails if :py:exec:`ValueError` wasn't raised when calling the function with a contract with invalid values."""
        with self.assertRaises(ValueError):
            kwargs = {
                "customer_profile_id": 1,
                "contract": apicontractsv1.customerPaymentProfileExType(
                    payment=apicontractsv1.paymentType(),
                    billTo=apicontractsv1.customerAddressType(),
                    customerPaymentProfileId=None,
                    defaultPaymentProfile="1",
                ),
                "validation": "testMode",
            }
            self.func(**kwargs)
        with self.assertRaises(ValueError):
            kwargs = {
                "customer_profile_id": 1,
                "contract": apicontractsv1.customerPaymentProfileExType(
                    payment=None,
                    billTo=apicontractsv1.customerAddressType(),
                    customerPaymentProfileId="1",
                    defaultPaymentProfile="1",
                ),
                "validation": "testMode",
            }
            self.func(**kwargs)
        with self.assertRaises(ValueError):
            kwargs = {
                "customer_profile_id": 1,
                "contract": apicontractsv1.customerPaymentProfileExType(
                    payment=apicontractsv1.paymentType(),
                    billTo=None,
                    customerPaymentProfileId="1",
                    defaultPaymentProfile="1",
                ),
                "validation": "testMode",
            }
            self.func(**kwargs)


class DeleteCustomerPaymentProfileFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.delete_customer_payment_profile

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        expected = apicontrollers.deleteCustomerPaymentProfileController
        kwargs = {"customer_profile_id": 1, "payment_profile_id": 1}
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {"customer_profile_id": 1, "payment_profile_id": 1}
        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.customerProfileId, str(kwargs["customer_profile_id"])
        )
        self.assertEqual(
            request.customerPaymentProfileId, str(kwargs["payment_profile_id"])
        )


class CreateSubscriptionFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.create_subscription

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {"contract": apicontractsv1.ARBSubscriptionType()}
        expected = apicontrollers.ARBCreateSubscriptionController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {"contract": apicontractsv1.ARBSubscriptionType()}
        request, _ = self.func(**kwargs)
        self.assertEqual(request.subscription, kwargs["contract"])


class GetSubscriptionFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.get_subscription

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {"subscription_id": 1, "include_transactions": False}
        expected = apicontrollers.ARBGetSubscriptionController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {"subscription_id": 1, "include_transactions": False}
        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.subscriptionId, str(kwargs["subscription_id"])
        )
        self.assertEqual(
            request.includeTransactions, int(kwargs["include_transactions"])
        )


class GetSubscriptionStatusFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.get_subscription_status

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {"subscription_id": 1}
        expected = apicontrollers.ARBGetSubscriptionStatusController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {"subscription_id": 1}
        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.subscriptionId, str(kwargs["subscription_id"])
        )


class UpdateSubscriptionFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.update_subscription

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {
            "subscription_id": 1,
            "contract": apicontractsv1.ARBSubscriptionType(),
        }
        expected = apicontrollers.ARBUpdateSubscriptionController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {
            "subscription_id": 1,
            "contract": apicontractsv1.ARBSubscriptionType(),
        }
        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.subscriptionId, str(kwargs["subscription_id"])
        )
        self.assertEqual(request.subscription, kwargs["contract"])


class CancelSubscriptionFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.func = api.cancel_subscription

    def test_controller_type(self):
        """Fails if the function returned an Authorizenet API controller of the incorrect type."""
        kwargs = {"subscription_id": 1}
        expected = apicontrollers.ARBCancelSubscriptionController
        _, controller = self.func(**kwargs)
        self.assertIs(controller, expected)

    def test_required_args_added_to_request(self):
        """Fails if any required arguments weren't present in the request contract."""
        kwargs = {"subscription_id": 1}
        request, _ = self.func(**kwargs)
        self.assertEqual(
            request.subscriptionId, str(kwargs["subscription_id"])
        )
