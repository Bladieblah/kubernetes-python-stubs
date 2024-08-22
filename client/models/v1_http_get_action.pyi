import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1HTTPGetAction:
    host: typing.Optional[str]
    http_headers: typing.Optional[list[kubernetes.client.V1HTTPHeader]]
    path: typing.Optional[str]
    port: typing.Any
    scheme: typing.Optional[str]
    def __init__(
        self,
        *,
        host: typing.Optional[str] = ...,
        http_headers: typing.Optional[list[kubernetes.client.V1HTTPHeader]] = ...,
        path: typing.Optional[str] = ...,
        port: typing.Any,
        scheme: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
