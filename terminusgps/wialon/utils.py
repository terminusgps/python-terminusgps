import secrets
import string

from terminusgps.wialon.session import WialonSession


def get_id_from_imei(session: WialonSession, imei: str) -> int:
    """
    Returns a Wialon unit ID from an IMEI (sys_unique_id) number.

    :param session: A valid Wialon API session.
    :type session: ~terminusgps.wialon.session.WialonSession
    :param imei: An IMEI number.
    :type imei: str
    :returns: A Wialon unit ID.
    :rtype: int

    """
    response = session.wialon_api.core_search_items(
        **{
            "spec": {
                "itemsType": "avl_unit",
                "propName": "sys_unique_id",
                "propValueMask": imei,
                "sortType": "sys_name",
                "propType": "property",
            },
            "force": 0,
            "flags": 1,
            "from": 0,
            "to": 0,
        }
    )
    if int(response["totalItemsCount"]) != 1:
        raise ValueError(f"Multiple items returned for IMEI #{imei}.")
    return int(response["items"][0]["id"])


def generate_wialon_password(length: int = 32) -> str:
    """
    Generates a Wialon compliant password between ``8`` and ``64`` characters.

    The generated password will contain:

        - At least one uppercase letter.
        - At least one lowercase letter.
        - At least one special symbol.
        - At least three digits.

    :param length: Length of the generated password. Default is ``32``.
    :type length: int
    :raises ValueError: If ``length`` was less than ``8`` or greater than ``64``.
    :returns: A Wialon compliant password.
    :rtype: str

    """
    min_length, max_length = 8, 64
    if length > max_length:
        raise ValueError(
            f"Password cannot be greater than {max_length} characters in length, got {length}."
        )
    elif length < min_length:
        raise ValueError(
            f"Password cannot be less than {min_length} characters in length, got {length}."
        )

    s0 = list(string.ascii_uppercase)
    s1 = list(string.ascii_lowercase)
    s2 = list(string.digits)
    s3 = list("!@#$%^*()[]-_+")

    while True:
        password = "".join(
            [secrets.choice(s0 + s1 + s2 + s3) for _ in range(length)]
        )
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
            and any(c in s3 for c in password)
        ):
            break
    return password
