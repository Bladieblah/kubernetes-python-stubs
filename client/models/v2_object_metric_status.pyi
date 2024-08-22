import typing

import kubernetes.client

class V2ObjectMetricStatus:
    current: kubernetes.client.V2MetricValueStatus
    described_object: kubernetes.client.V2CrossVersionObjectReference
    metric: kubernetes.client.V2MetricIdentifier
    def __init__(
        self,
        *,
        current: kubernetes.client.V2MetricValueStatus,
        described_object: kubernetes.client.V2CrossVersionObjectReference,
        metric: kubernetes.client.V2MetricIdentifier,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
