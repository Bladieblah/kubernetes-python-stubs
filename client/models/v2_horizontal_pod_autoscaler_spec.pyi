import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2HorizontalPodAutoscalerSpec:
    behavior: typing.Optional[kubernetes.client.V2HorizontalPodAutoscalerBehavior]
    max_replicas: int
    metrics: typing.Optional[list[kubernetes.client.V2MetricSpec]]
    min_replicas: typing.Optional[int]
    scale_target_ref: kubernetes.client.V2CrossVersionObjectReference
    def __init__(
        self,
        *,
        behavior: typing.Optional[kubernetes.client.V2HorizontalPodAutoscalerBehavior] = ...,
        max_replicas: int,
        metrics: typing.Optional[list[kubernetes.client.V2MetricSpec]] = ...,
        min_replicas: typing.Optional[int] = ...,
        scale_target_ref: kubernetes.client.V2CrossVersionObjectReference,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
