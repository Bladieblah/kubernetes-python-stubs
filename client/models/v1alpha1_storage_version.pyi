import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha1StorageVersion:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Any
    status: kubernetes.client.V1alpha1StorageVersionStatus
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Any,
        status: kubernetes.client.V1alpha1StorageVersionStatus,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
