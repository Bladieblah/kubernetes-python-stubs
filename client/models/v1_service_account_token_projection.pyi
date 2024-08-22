import typing
from urllib3 import BaseHTTPResponse

class V1ServiceAccountTokenProjection:
    audience: typing.Optional[str]
    expiration_seconds: typing.Optional[int]
    path: str
    def __init__(
        self, *, audience: typing.Optional[str] = ..., expiration_seconds: typing.Optional[int] = ..., path: str
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
