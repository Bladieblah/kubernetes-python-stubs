import typing
from urllib3 import BaseHTTPResponse

class V1ExemptPriorityLevelConfiguration:
    lendable_percent: typing.Optional[int]
    nominal_concurrency_shares: typing.Optional[int]
    def __init__(
        self, *, lendable_percent: typing.Optional[int] = ..., nominal_concurrency_shares: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
