import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CertificateSigningRequest:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1CertificateSigningRequestSpec
    status: typing.Optional[kubernetes.client.V1CertificateSigningRequestStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1CertificateSigningRequestSpec,
        status: typing.Optional[kubernetes.client.V1CertificateSigningRequestStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
