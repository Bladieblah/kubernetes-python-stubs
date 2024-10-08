import typing

import kubernetes.client

class V1ReplicaSet:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1ReplicaSetSpec]
    status: typing.Optional[kubernetes.client.V1ReplicaSetStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1ReplicaSetSpec] = ...,
        status: typing.Optional[kubernetes.client.V1ReplicaSetStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
