import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2MetricIdentifier:
    name: str
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    def __init__(self, *, name: str, selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
