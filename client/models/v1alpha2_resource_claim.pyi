import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha2ResourceClaim:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1alpha2ResourceClaimSpec
    status: typing.Optional[kubernetes.client.V1alpha2ResourceClaimStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha2ResourceClaimSpec,
        status: typing.Optional[kubernetes.client.V1alpha2ResourceClaimStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
