import typing
from urllib3 import BaseHTTPResponse

class V1SELinuxOptions:
    level: typing.Optional[str]
    role: typing.Optional[str]
    type: typing.Optional[str]
    user: typing.Optional[str]
    def __init__(
        self,
        *,
        level: typing.Optional[str] = ...,
        role: typing.Optional[str] = ...,
        type: typing.Optional[str] = ...,
        user: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
