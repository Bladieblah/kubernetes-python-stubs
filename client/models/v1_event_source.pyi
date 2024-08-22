import typing
from urllib3 import BaseHTTPResponse

class V1EventSource:
    component: typing.Optional[str]
    host: typing.Optional[str]
    def __init__(self, *, component: typing.Optional[str] = ..., host: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
