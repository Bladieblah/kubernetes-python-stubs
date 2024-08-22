import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ValidatingAdmissionPolicyStatus:
    conditions: typing.Optional[list[kubernetes.client.V1Condition]]
    observed_generation: typing.Optional[int]
    type_checking: typing.Optional[kubernetes.client.V1TypeChecking]
    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes.client.V1Condition]] = ...,
        observed_generation: typing.Optional[int] = ...,
        type_checking: typing.Optional[kubernetes.client.V1TypeChecking] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
