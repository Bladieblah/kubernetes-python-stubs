import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CustomResourceSubresources:
    scale: typing.Optional[kubernetes.client.V1CustomResourceSubresourceScale]
    status: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        scale: typing.Optional[kubernetes.client.V1CustomResourceSubresourceScale] = ...,
        status: typing.Optional[typing.Any] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
