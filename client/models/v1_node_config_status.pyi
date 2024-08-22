import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1NodeConfigStatus:
    active: typing.Optional[kubernetes.client.V1NodeConfigSource]
    assigned: typing.Optional[kubernetes.client.V1NodeConfigSource]
    error: typing.Optional[str]
    last_known_good: typing.Optional[kubernetes.client.V1NodeConfigSource]
    def __init__(
        self,
        *,
        active: typing.Optional[kubernetes.client.V1NodeConfigSource] = ...,
        assigned: typing.Optional[kubernetes.client.V1NodeConfigSource] = ...,
        error: typing.Optional[str] = ...,
        last_known_good: typing.Optional[kubernetes.client.V1NodeConfigSource] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
