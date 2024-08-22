import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CertificateSigningRequestStatus:
    certificate: typing.Optional[str]
    conditions: typing.Optional[list[kubernetes.client.V1CertificateSigningRequestCondition]]
    def __init__(
        self,
        *,
        certificate: typing.Optional[str] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1CertificateSigningRequestCondition]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
