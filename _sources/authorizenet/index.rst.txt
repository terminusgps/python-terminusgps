Authorizenet
============

The :py:mod:`terminusgps.authorizenet` package provides convenient functions for interacting with the Authorizenet API in a Pythonic interface.

These functions may be executed via the :py:meth:`~terminusgps.authorizenet.services.AuthorizenetService.request` method on a service instance.

Most `Authorizenet API endpoints <https://developer.authorize.net/api/reference/index.html>`_ are represented as plain Python functions.

.. attention:: These functions require the following settings to be present in your Django project's ``settings.py`` module.

   Using this package without setting these settings will raise :py:exc:`~django.core.exceptions.ImproperlyConfigured`.

   +-----------------------------------+---------------+
   | setting                           | type          |
   +===================================+===============+
   | ``MERCHANT_AUTH_ENVIRONMENT``     | :py:obj:`str` |
   +-----------------------------------+---------------+
   | ``MERCHANT_AUTH_LOGIN_ID``        | :py:obj:`str` |
   +-----------------------------------+---------------+
   | ``MERCHANT_AUTH_TRANSACTION_KEY`` | :py:obj:`str` |
   +-----------------------------------+---------------+
   | ``MERCHANT_AUTH_VALIDATION_MODE`` | :py:obj:`str` |
   +-----------------------------------+---------------+

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    auth.rst
    constants.rst
    exceptions.rst
    api.rst
    usage.rst
    services.rst
