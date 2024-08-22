import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1IngressServiceBackend:
    name: str
    port: typing.Optional[kubernetes.client.V1ServiceBackendPort]
    def __init__(self, *, name: str, port: typing.Optional[kubernetes.client.V1ServiceBackendPort] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
