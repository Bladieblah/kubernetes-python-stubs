import typing

import kubernetes.client

class V1Namespace:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1NamespaceSpec]
    status: typing.Optional[kubernetes.client.V1NamespaceStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1NamespaceSpec] = ...,
        status: typing.Optional[kubernetes.client.V1NamespaceStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
