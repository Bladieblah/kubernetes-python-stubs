import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1NetworkPolicyIngressRule:
    _from: typing.Optional[list[kubernetes.client.V1NetworkPolicyPeer]]
    ports: typing.Optional[list[kubernetes.client.V1NetworkPolicyPort]]
    def __init__(
        self,
        *,
        _from: typing.Optional[list[kubernetes.client.V1NetworkPolicyPeer]] = ...,
        ports: typing.Optional[list[kubernetes.client.V1NetworkPolicyPort]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
