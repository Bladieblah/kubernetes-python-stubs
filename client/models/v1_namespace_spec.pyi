import typing
from urllib3 import BaseHTTPResponse

class V1NamespaceSpec:
    finalizers: typing.Optional[list[str]]
    def __init__(self, *, finalizers: typing.Optional[list[str]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
