import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2ResourceMetricStatus:
    current: kubernetes.client.V2MetricValueStatus
    name: str
    def __init__(self, *, current: kubernetes.client.V2MetricValueStatus, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
