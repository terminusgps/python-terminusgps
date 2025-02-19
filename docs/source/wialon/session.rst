Wialon API Sessions
===================

.. currentmodule:: terminusgps.wialon.session

.. py:class:: WialonSession

    Starts or continues a Wialon API session.

    :param token: An optional Wialon API token. Default is :confval:`WIALON_TOKEN`.
    :type token: :py:obj:`str` | :py:obj:`None`
    :param sid: An optional Wialon API session id. If provided, the session is continued.
    :type sid: :py:obj:`str` | :py:obj:`None`
    :param scheme: HTTP request scheme to use. Default is ``"https"``.
    :type scheme: :py:obj:`str`
    :param host: Wialon API host url. Default is ``"hst-api.wialon.com"``.
    :type host: :py:obj:`str`
    :param port: Wialon API host port. Default is ``443``.
    :type port: :py:obj:`int`
    :param log_level: Severity level at which log messages should be handled. Default is ``20`` (logging.INFO).
    :type log_level: :py:obj:`int`


    .. py:property:: gis_geocode

        GIS geocode URL.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: gis_render

        GIS renderer URL.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: gis_routing

        GIS routing URL.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: gis_search

        GIS searching URL.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: gis_sid

        GIS session id.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: host

        Client IP address.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: hw_gw_ip

        Hardware gateway ip.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: hw_gw_dns

        Hardware gateway domain name.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: wsdk_version

        Wialon Source Developer Kit (wsdk) version.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: uid

        Wialon user id the session is operating as.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: username

        Wialon username the session is operating as.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:property:: token

        A Wialon API token set during :py:meth:`~WialonSession.__init__`.

        :type: :py:obj:`str` | :py:obj:`None`
        :value: :py:obj:`None`

    .. py:method:: login(token, [flags,]) -> str

        Logs into the Wialon API, sets session attributes, and returns a session id.

        :param token: An activated Wialon API token.
        :type token: :py:obj:`str`
        :param flags: A login response flag integer. Default is ``35``.
        :type flags: :py:obj:`int`
        :raises WialonError: If the login fails.
        :raises AssertionError: If the login token was not set.
        :returns: The new session id.
        :rtype: :py:obj:`str`

    .. py:method:: logout() -> None

        Logs out of the Wialon API session.

        :raises WialonError: If something goes wrong during a Wialon API call.
        :returns: Nothing.
        :rtype: :py:obj:`None`

=====
Usage
=====

.. code:: python

    from terminusgps.wialon.session import WialonSession

    # Create a session and login to it
    session = WialonSession()
    session.login(token="my_secure_token")

    # Use the logged in session to perform API actions
    session.wialon_api.core_search_item(**{"id": "123", "flags": 1})

    # Don't forget to logout of the session
    # Sessions are destroyed after 5min of inactivity
    session.logout()

    # Alternatively, use a context manager
    # The context manager handles logging in and out of the session.
    with WialonSession() as session:
        session.wialon_api.core_search_item(**{"id": "123", "flags": 1})

    # If you already have a session id, no need to login again
    session = WialonSession(sid="my_valid_session_id")
    session.wialon_api.core_search_item(**{"id": "123", "flags": 1})
