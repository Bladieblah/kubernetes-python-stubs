import typing

import kubernetes.client

class V1alpha2PodSchedulingContextList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.V1alpha2PodSchedulingContext]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1alpha2PodSchedulingContext],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
