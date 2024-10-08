import typing

import kubernetes.client

class V1ResourceQuota:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1ResourceQuotaSpec]
    status: typing.Optional[kubernetes.client.V1ResourceQuotaStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1ResourceQuotaSpec] = ...,
        status: typing.Optional[kubernetes.client.V1ResourceQuotaStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
