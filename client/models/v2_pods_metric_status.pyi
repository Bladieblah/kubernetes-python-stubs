import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2PodsMetricStatus:
    current: kubernetes.client.V2MetricValueStatus
    metric: kubernetes.client.V2MetricIdentifier
    def __init__(
        self, *, current: kubernetes.client.V2MetricValueStatus, metric: kubernetes.client.V2MetricIdentifier
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
