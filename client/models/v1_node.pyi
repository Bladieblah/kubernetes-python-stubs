import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1Node:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1NodeSpec]
    status: typing.Optional[kubernetes.client.V1NodeStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1NodeSpec] = ...,
        status: typing.Optional[kubernetes.client.V1NodeStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
