import typing

import kubernetes.client

class V2PodsMetricSource:
    metric: kubernetes.client.V2MetricIdentifier
    target: kubernetes.client.V2MetricTarget
    def __init__(
        self, *, metric: kubernetes.client.V2MetricIdentifier, target: kubernetes.client.V2MetricTarget
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
