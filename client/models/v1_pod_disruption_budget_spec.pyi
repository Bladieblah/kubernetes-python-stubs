import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1PodDisruptionBudgetSpec:
    max_unavailable: typing.Optional[typing.Any]
    min_available: typing.Optional[typing.Any]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    unhealthy_pod_eviction_policy: typing.Optional[str]
    def __init__(
        self,
        *,
        max_unavailable: typing.Optional[typing.Any] = ...,
        min_available: typing.Optional[typing.Any] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        unhealthy_pod_eviction_policy: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
