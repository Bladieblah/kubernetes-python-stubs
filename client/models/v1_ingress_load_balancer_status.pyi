import typing

import kubernetes.client

class V1IngressLoadBalancerStatus:
    ingress: typing.Optional[list[kubernetes.client.V1IngressLoadBalancerIngress]]
    def __init__(
        self, *, ingress: typing.Optional[list[kubernetes.client.V1IngressLoadBalancerIngress]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
