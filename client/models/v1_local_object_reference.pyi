import typing
from urllib3 import BaseHTTPResponse

class V1LocalObjectReference:
    name: typing.Optional[str]
    def __init__(self, *, name: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
