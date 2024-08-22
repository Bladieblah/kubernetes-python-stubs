import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1beta3FlowSchema:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta3FlowSchemaSpec]
    status: typing.Optional[kubernetes.client.V1beta3FlowSchemaStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1beta3FlowSchemaSpec] = ...,
        status: typing.Optional[kubernetes.client.V1beta3FlowSchemaStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
