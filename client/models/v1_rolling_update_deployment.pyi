import typing
from urllib3 import BaseHTTPResponse

class V1RollingUpdateDeployment:
    max_surge: typing.Optional[typing.Any]
    max_unavailable: typing.Optional[typing.Any]
    def __init__(
        self, *, max_surge: typing.Optional[typing.Any] = ..., max_unavailable: typing.Optional[typing.Any] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
