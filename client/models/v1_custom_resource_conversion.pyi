import typing

import kubernetes.client

class V1CustomResourceConversion:
    strategy: str
    webhook: typing.Optional[kubernetes.client.V1WebhookConversion]
    def __init__(
        self, *, strategy: str, webhook: typing.Optional[kubernetes.client.V1WebhookConversion] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
