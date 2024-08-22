import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1Eviction:
    api_version: typing.Optional[str]
    delete_options: typing.Optional[kubernetes.client.V1DeleteOptions]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        delete_options: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
