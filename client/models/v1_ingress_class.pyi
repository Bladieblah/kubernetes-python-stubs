import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1IngressClass:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1IngressClassSpec]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1IngressClassSpec] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
