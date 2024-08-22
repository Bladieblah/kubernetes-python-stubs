import typing

import kubernetes.client

class V1beta3Subject:
    group: typing.Optional[kubernetes.client.V1beta3GroupSubject]
    kind: str
    service_account: typing.Optional[kubernetes.client.V1beta3ServiceAccountSubject]
    user: typing.Optional[kubernetes.client.V1beta3UserSubject]
    def __init__(
        self,
        *,
        group: typing.Optional[kubernetes.client.V1beta3GroupSubject] = ...,
        kind: str,
        service_account: typing.Optional[kubernetes.client.V1beta3ServiceAccountSubject] = ...,
        user: typing.Optional[kubernetes.client.V1beta3UserSubject] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
