import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class ApiextensionsV1WebhookClientConfig:
    ca_bundle: typing.Optional[str]
    service: typing.Optional[kubernetes.client.ApiextensionsV1ServiceReference]
    url: typing.Optional[str]
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        service: typing.Optional[kubernetes.client.ApiextensionsV1ServiceReference] = ...,
        url: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
