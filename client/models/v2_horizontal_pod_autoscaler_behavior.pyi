import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2HorizontalPodAutoscalerBehavior:
    scale_down: typing.Optional[kubernetes.client.V2HPAScalingRules]
    scale_up: typing.Optional[kubernetes.client.V2HPAScalingRules]
    def __init__(
        self,
        *,
        scale_down: typing.Optional[kubernetes.client.V2HPAScalingRules] = ...,
        scale_up: typing.Optional[kubernetes.client.V2HPAScalingRules] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
