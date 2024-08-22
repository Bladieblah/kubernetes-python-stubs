import typing
from urllib3 import BaseHTTPResponse

class V1PodDNSConfigOption:
    name: typing.Optional[str]
    value: typing.Optional[str]
    def __init__(self, *, name: typing.Optional[str] = ..., value: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
