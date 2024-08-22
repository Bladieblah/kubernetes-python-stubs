import datetime
import typing
from urllib3 import BaseHTTPResponse

class V1TokenRequestStatus:
    expiration_timestamp: datetime.datetime
    token: str
    def __init__(self, *, expiration_timestamp: datetime.datetime, token: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
