import typing
from urllib3 import BaseHTTPResponse

class V1RollingUpdateStatefulSetStrategy:
    max_unavailable: typing.Optional[typing.Any]
    partition: typing.Optional[int]
    def __init__(
        self, *, max_unavailable: typing.Optional[typing.Any] = ..., partition: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
