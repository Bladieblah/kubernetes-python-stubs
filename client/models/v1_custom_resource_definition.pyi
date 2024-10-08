import typing

import kubernetes.client

class V1CustomResourceDefinition:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1CustomResourceDefinitionSpec
    status: typing.Optional[kubernetes.client.V1CustomResourceDefinitionStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1CustomResourceDefinitionSpec,
        status: typing.Optional[kubernetes.client.V1CustomResourceDefinitionStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
