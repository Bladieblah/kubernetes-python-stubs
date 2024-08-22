import typing
from urllib3 import BaseHTTPResponse

class V1HostAlias:
    hostnames: typing.Optional[list[str]]
    ip: str
    def __init__(self, *, hostnames: typing.Optional[list[str]] = ..., ip: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
