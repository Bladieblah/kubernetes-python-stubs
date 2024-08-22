import typing

import kubernetes.client

class V1alpha1StorageVersionMigration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1alpha1StorageVersionMigrationSpec]
    status: typing.Optional[kubernetes.client.V1alpha1StorageVersionMigrationStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1alpha1StorageVersionMigrationSpec] = ...,
        status: typing.Optional[kubernetes.client.V1alpha1StorageVersionMigrationStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
