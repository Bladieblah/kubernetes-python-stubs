import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha1StorageVersionMigrationSpec:
    continue_token: typing.Optional[str]
    resource: kubernetes.client.V1alpha1GroupVersionResource
    def __init__(
        self, *, continue_token: typing.Optional[str] = ..., resource: kubernetes.client.V1alpha1GroupVersionResource
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
