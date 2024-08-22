import typing
from urllib3 import BaseHTTPResponse

class V1alpha1ServiceCIDRSpec:
    cidrs: typing.Optional[list[str]]
    def __init__(self, *, cidrs: typing.Optional[list[str]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
