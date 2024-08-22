import typing
from urllib3 import BaseHTTPResponse

class V1HostIP:
    ip: typing.Optional[str]
    def __init__(self, *, ip: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
