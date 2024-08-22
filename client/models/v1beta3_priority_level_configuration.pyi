import typing

import kubernetes.client

class V1beta3PriorityLevelConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta3PriorityLevelConfigurationSpec]
    status: typing.Optional[kubernetes.client.V1beta3PriorityLevelConfigurationStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1beta3PriorityLevelConfigurationSpec] = ...,
        status: typing.Optional[kubernetes.client.V1beta3PriorityLevelConfigurationStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
