import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1NamespaceStatus:
    conditions: typing.Optional[list[kubernetes.client.V1NamespaceCondition]]
    phase: typing.Optional[str]
    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes.client.V1NamespaceCondition]] = ...,
        phase: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
