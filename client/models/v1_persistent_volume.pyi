import typing

import kubernetes.client

class V1PersistentVolume:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1PersistentVolumeSpec]
    status: typing.Optional[kubernetes.client.V1PersistentVolumeStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1PersistentVolumeSpec] = ...,
        status: typing.Optional[kubernetes.client.V1PersistentVolumeStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
