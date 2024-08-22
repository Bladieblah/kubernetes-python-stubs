import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2ContainerResourceMetricSource:
    container: str
    name: str
    target: kubernetes.client.V2MetricTarget
    def __init__(self, *, container: str, name: str, target: kubernetes.client.V2MetricTarget) -> None: ...
    def to_dict(self) -> typing.Any: ...
