import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1beta1ValidatingAdmissionPolicyBindingList:
    api_version: typing.Optional[str]
    items: typing.Optional[list[kubernetes.client.V1beta1ValidatingAdmissionPolicyBinding]]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.Optional[list[kubernetes.client.V1beta1ValidatingAdmissionPolicyBinding]] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
