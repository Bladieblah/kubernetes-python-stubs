import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1IngressStatus:
    load_balancer: typing.Optional[kubernetes.client.V1IngressLoadBalancerStatus]
    def __init__(
        self, *, load_balancer: typing.Optional[kubernetes.client.V1IngressLoadBalancerStatus] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
