import typing

import kubernetes.client

class V1alpha2ResourceClaimTemplate:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1alpha2ResourceClaimTemplateSpec
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha2ResourceClaimTemplateSpec,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
