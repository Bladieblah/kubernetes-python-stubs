import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1Binding:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    target: kubernetes.client.V1ObjectReference
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        target: kubernetes.client.V1ObjectReference,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
