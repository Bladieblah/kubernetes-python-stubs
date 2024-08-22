import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ClusterRoleBinding:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    role_ref: kubernetes.client.V1RoleRef
    subjects: typing.Optional[list[kubernetes.client.RbacV1Subject]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        role_ref: kubernetes.client.V1RoleRef,
        subjects: typing.Optional[list[kubernetes.client.RbacV1Subject]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
