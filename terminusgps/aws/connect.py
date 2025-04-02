import jwt
import datetime

from django.conf import settings

def get_aws_connect_jwt(widget_id: str, expires_in: int = 500) -> str:
    payload = {
        "sub": widget_id,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() - datetime.timedelta(seconds=expires_in),
        "customerId": "",
        "segmentAttributes": {"connect:Subtype": {"ValueString" : "connect:Guide"}}, 'attributes': {"name": "Jane", "memberID": "123456789", "email": "Jane@example.com", "isPremiumUser": "true", "age": "45"} },
    }
    header = {"typ": "JWT", "alg": "HS256"}
    encoded_token = jwt.encode((payload), settings.CONNECT_SECRET, algorithm=header["alg"], headers=header)
    return encoded_token
