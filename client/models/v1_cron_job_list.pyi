import typing

import kubernetes.client

class V1CronJobList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.V1CronJob]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1CronJob],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
