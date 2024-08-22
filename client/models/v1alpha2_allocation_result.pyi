import typing

import kubernetes.client

class V1alpha2AllocationResult:
    available_on_nodes: typing.Optional[kubernetes.client.V1NodeSelector]
    resource_handles: typing.Optional[list[kubernetes.client.V1alpha2ResourceHandle]]
    shareable: typing.Optional[bool]
    def __init__(
        self,
        *,
        available_on_nodes: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        resource_handles: typing.Optional[list[kubernetes.client.V1alpha2ResourceHandle]] = ...,
        shareable: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
