import typing
from urllib3 import BaseHTTPResponse

class V1TCPSocketAction:
    host: typing.Optional[str]
    port: typing.Any
    def __init__(self, *, host: typing.Optional[str] = ..., port: typing.Any) -> None: ...
    def to_dict(self) -> typing.Any: ...
