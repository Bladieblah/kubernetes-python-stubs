import typing
from urllib3 import BaseHTTPResponse

class ApiextensionsV1ServiceReference:
    name: str
    namespace: str
    path: typing.Optional[str]
    port: typing.Optional[int]
    def __init__(
        self, *, name: str, namespace: str, path: typing.Optional[str] = ..., port: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
