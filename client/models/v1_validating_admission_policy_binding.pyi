import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ValidatingAdmissionPolicyBinding:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1ValidatingAdmissionPolicyBindingSpec]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1ValidatingAdmissionPolicyBindingSpec] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
