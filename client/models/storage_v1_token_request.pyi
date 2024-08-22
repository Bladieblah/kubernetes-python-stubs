import typing
from urllib3 import BaseHTTPResponse

class StorageV1TokenRequest:
    audience: str
    expiration_seconds: typing.Optional[int]
    def __init__(self, *, audience: str, expiration_seconds: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
