import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CSINode:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1CSINodeSpec
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1CSINodeSpec,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
