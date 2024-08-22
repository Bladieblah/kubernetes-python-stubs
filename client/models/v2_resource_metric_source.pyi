import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2ResourceMetricSource:
    name: str
    target: kubernetes.client.V2MetricTarget
    def __init__(self, *, name: str, target: kubernetes.client.V2MetricTarget) -> None: ...
    def to_dict(self) -> typing.Any: ...
