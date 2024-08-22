import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1IngressLoadBalancerIngress:
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ports: typing.Optional[list[kubernetes.client.V1IngressPortStatus]]
    def __init__(
        self,
        *,
        hostname: typing.Optional[str] = ...,
        ip: typing.Optional[str] = ...,
        ports: typing.Optional[list[kubernetes.client.V1IngressPortStatus]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
