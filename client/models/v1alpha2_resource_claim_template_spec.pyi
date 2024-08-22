import typing

import kubernetes.client

class V1alpha2ResourceClaimTemplateSpec:
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1alpha2ResourceClaimSpec
    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha2ResourceClaimSpec,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
