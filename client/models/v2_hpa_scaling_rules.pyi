import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2HPAScalingRules:
    policies: typing.Optional[list[kubernetes.client.V2HPAScalingPolicy]]
    select_policy: typing.Optional[str]
    stabilization_window_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        policies: typing.Optional[list[kubernetes.client.V2HPAScalingPolicy]] = ...,
        select_policy: typing.Optional[str] = ...,
        stabilization_window_seconds: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
