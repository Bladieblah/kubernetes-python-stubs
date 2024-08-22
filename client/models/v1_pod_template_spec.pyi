import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1PodTemplateSpec:
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1PodSpec]
    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1PodSpec] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
