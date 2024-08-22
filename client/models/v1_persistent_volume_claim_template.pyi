import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1PersistentVolumeClaimTemplate:
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1PersistentVolumeClaimSpec
    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1PersistentVolumeClaimSpec,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
