import typing
from urllib3 import BaseHTTPResponse

class V1SuccessPolicyRule:
    succeeded_count: typing.Optional[int]
    succeeded_indexes: typing.Optional[str]
    def __init__(
        self, *, succeeded_count: typing.Optional[int] = ..., succeeded_indexes: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
