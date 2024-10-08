import typing

import kubernetes.client

class V1alpha2ResourceSlice:
    api_version: typing.Optional[str]
    driver_name: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesResources]
    node_name: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        driver_name: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesResources] = ...,
        node_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
