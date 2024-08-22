import typing
from urllib3 import BaseHTTPResponse

class V1ServiceBackendPort:
    name: typing.Optional[str]
    number: typing.Optional[int]
    def __init__(self, *, name: typing.Optional[str] = ..., number: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
