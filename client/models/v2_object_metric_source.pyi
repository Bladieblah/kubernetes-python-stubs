import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2ObjectMetricSource:
    described_object: kubernetes.client.V2CrossVersionObjectReference
    metric: kubernetes.client.V2MetricIdentifier
    target: kubernetes.client.V2MetricTarget
    def __init__(
        self,
        *,
        described_object: kubernetes.client.V2CrossVersionObjectReference,
        metric: kubernetes.client.V2MetricIdentifier,
        target: kubernetes.client.V2MetricTarget,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
