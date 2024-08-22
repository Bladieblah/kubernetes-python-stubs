import typing

import kubernetes.client

class V1Endpoint:
    addresses: list[str]
    conditions: typing.Optional[kubernetes.client.V1EndpointConditions]
    deprecated_topology: typing.Optional[dict[str, str]]
    hints: typing.Optional[kubernetes.client.V1EndpointHints]
    hostname: typing.Optional[str]
    node_name: typing.Optional[str]
    target_ref: typing.Optional[kubernetes.client.V1ObjectReference]
    zone: typing.Optional[str]
    def __init__(
        self,
        *,
        addresses: list[str],
        conditions: typing.Optional[kubernetes.client.V1EndpointConditions] = ...,
        deprecated_topology: typing.Optional[dict[str, str]] = ...,
        hints: typing.Optional[kubernetes.client.V1EndpointHints] = ...,
        hostname: typing.Optional[str] = ...,
        node_name: typing.Optional[str] = ...,
        target_ref: typing.Optional[kubernetes.client.V1ObjectReference] = ...,
        zone: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
