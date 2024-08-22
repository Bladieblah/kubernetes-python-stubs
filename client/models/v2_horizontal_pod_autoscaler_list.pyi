import typing

import kubernetes.client

class V2HorizontalPodAutoscalerList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.V2HorizontalPodAutoscaler]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V2HorizontalPodAutoscaler],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
