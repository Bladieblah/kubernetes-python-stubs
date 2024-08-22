import datetime
import typing

class V1TokenRequestStatus:
    expiration_timestamp: datetime.datetime
    token: str
    def __init__(self, *, expiration_timestamp: datetime.datetime, token: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
