Usage
=====

Check the Authorizenet API documentation for expected attributes in each response.

.. code:: python

    from terminusgps.authorizenet import api
    from terminusgps.authorizenet.services import AuthorizenetService

    service = AuthorizenetService()
    response = service.request(
        api.create_customer_profile,
        merchant_id=str(67),
        email="peter@terminusgps.com"
    )
    response.customerProfileId # Authorizenet generated customer profile id
