import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1JobTemplateSpec:
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1JobSpec]
    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1JobSpec] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
