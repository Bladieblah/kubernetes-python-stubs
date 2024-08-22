import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1EndpointAddress:
    hostname: typing.Optional[str]
    ip: str
    node_name: typing.Optional[str]
    target_ref: typing.Optional[kubernetes.client.V1ObjectReference]
    def __init__(
        self,
        *,
        hostname: typing.Optional[str] = ...,
        ip: str,
        node_name: typing.Optional[str] = ...,
        target_ref: typing.Optional[kubernetes.client.V1ObjectReference] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
