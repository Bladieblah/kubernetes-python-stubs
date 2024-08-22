import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha1StorageVersionStatus:
    common_encoding_version: typing.Optional[str]
    conditions: typing.Optional[list[kubernetes.client.V1alpha1StorageVersionCondition]]
    storage_versions: typing.Optional[list[kubernetes.client.V1alpha1ServerStorageVersion]]
    def __init__(
        self,
        *,
        common_encoding_version: typing.Optional[str] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1alpha1StorageVersionCondition]] = ...,
        storage_versions: typing.Optional[list[kubernetes.client.V1alpha1ServerStorageVersion]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
