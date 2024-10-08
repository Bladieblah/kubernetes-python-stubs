import typing

import kubernetes.client

class V1ValidatingAdmissionPolicyList:
    api_version: typing.Optional[str]
    items: typing.Optional[list[kubernetes.client.V1ValidatingAdmissionPolicy]]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.Optional[list[kubernetes.client.V1ValidatingAdmissionPolicy]] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
