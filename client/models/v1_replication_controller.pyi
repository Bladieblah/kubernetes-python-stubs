import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ReplicationController:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1ReplicationControllerSpec]
    status: typing.Optional[kubernetes.client.V1ReplicationControllerStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1ReplicationControllerSpec] = ...,
        status: typing.Optional[kubernetes.client.V1ReplicationControllerStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
