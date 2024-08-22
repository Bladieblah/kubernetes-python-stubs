import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2ContainerResourceMetricStatus:
    container: str
    current: kubernetes.client.V2MetricValueStatus
    name: str
    def __init__(self, *, container: str, current: kubernetes.client.V2MetricValueStatus, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
