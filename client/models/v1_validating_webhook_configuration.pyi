import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ValidatingWebhookConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    webhooks: typing.Optional[list[kubernetes.client.V1ValidatingWebhook]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        webhooks: typing.Optional[list[kubernetes.client.V1ValidatingWebhook]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
