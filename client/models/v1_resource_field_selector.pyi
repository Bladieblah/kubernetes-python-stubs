import typing
from urllib3 import BaseHTTPResponse

class V1ResourceFieldSelector:
    container_name: typing.Optional[str]
    divisor: typing.Optional[str]
    resource: str
    def __init__(
        self, *, container_name: typing.Optional[str] = ..., divisor: typing.Optional[str] = ..., resource: str
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
