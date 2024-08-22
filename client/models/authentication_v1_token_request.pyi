import typing

import kubernetes.client

class AuthenticationV1TokenRequest:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1TokenRequestSpec
    status: typing.Optional[kubernetes.client.V1TokenRequestStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1TokenRequestSpec,
        status: typing.Optional[kubernetes.client.V1TokenRequestStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
