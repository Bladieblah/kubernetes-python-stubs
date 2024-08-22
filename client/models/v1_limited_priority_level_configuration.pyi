import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1LimitedPriorityLevelConfiguration:
    borrowing_limit_percent: typing.Optional[int]
    lendable_percent: typing.Optional[int]
    limit_response: typing.Optional[kubernetes.client.V1LimitResponse]
    nominal_concurrency_shares: typing.Optional[int]
    def __init__(
        self,
        *,
        borrowing_limit_percent: typing.Optional[int] = ...,
        lendable_percent: typing.Optional[int] = ...,
        limit_response: typing.Optional[kubernetes.client.V1LimitResponse] = ...,
        nominal_concurrency_shares: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
