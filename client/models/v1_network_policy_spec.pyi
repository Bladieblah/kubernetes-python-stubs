import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1NetworkPolicySpec:
    egress: typing.Optional[list[kubernetes.client.V1NetworkPolicyEgressRule]]
    ingress: typing.Optional[list[kubernetes.client.V1NetworkPolicyIngressRule]]
    pod_selector: kubernetes.client.V1LabelSelector
    policy_types: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        egress: typing.Optional[list[kubernetes.client.V1NetworkPolicyEgressRule]] = ...,
        ingress: typing.Optional[list[kubernetes.client.V1NetworkPolicyIngressRule]] = ...,
        pod_selector: kubernetes.client.V1LabelSelector,
        policy_types: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
