import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1NodeDaemonEndpoints:
    kubelet_endpoint: typing.Optional[kubernetes.client.V1DaemonEndpoint]
    def __init__(self, *, kubelet_endpoint: typing.Optional[kubernetes.client.V1DaemonEndpoint] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
