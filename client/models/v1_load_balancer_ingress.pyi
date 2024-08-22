import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1LoadBalancerIngress:
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ip_mode: typing.Optional[str]
    ports: typing.Optional[list[kubernetes.client.V1PortStatus]]
    def __init__(
        self,
        *,
        hostname: typing.Optional[str] = ...,
        ip: typing.Optional[str] = ...,
        ip_mode: typing.Optional[str] = ...,
        ports: typing.Optional[list[kubernetes.client.V1PortStatus]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
