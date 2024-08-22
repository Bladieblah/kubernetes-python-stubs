import typing
from urllib3 import BaseHTTPResponse

class V1ResourceQuotaStatus:
    hard: typing.Optional[dict[str, str]]
    used: typing.Optional[dict[str, str]]
    def __init__(
        self, *, hard: typing.Optional[dict[str, str]] = ..., used: typing.Optional[dict[str, str]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
