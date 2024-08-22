import typing

import kubernetes.client

class V1CronJob:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1CronJobSpec]
    status: typing.Optional[kubernetes.client.V1CronJobStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1CronJobSpec] = ...,
        status: typing.Optional[kubernetes.client.V1CronJobStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
