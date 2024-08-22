import typing
from urllib3 import BaseHTTPResponse

class V1ClientIPConfig:
    timeout_seconds: typing.Optional[int]
    def __init__(self, *, timeout_seconds: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
