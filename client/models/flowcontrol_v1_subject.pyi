import typing

import kubernetes.client

class FlowcontrolV1Subject:
    group: typing.Optional[kubernetes.client.V1GroupSubject]
    kind: str
    service_account: typing.Optional[kubernetes.client.V1ServiceAccountSubject]
    user: typing.Optional[kubernetes.client.V1UserSubject]
    def __init__(
        self,
        *,
        group: typing.Optional[kubernetes.client.V1GroupSubject] = ...,
        kind: str,
        service_account: typing.Optional[kubernetes.client.V1ServiceAccountSubject] = ...,
        user: typing.Optional[kubernetes.client.V1UserSubject] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
