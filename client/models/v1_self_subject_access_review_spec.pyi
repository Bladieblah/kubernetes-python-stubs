import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1SelfSubjectAccessReviewSpec:
    non_resource_attributes: typing.Optional[kubernetes.client.V1NonResourceAttributes]
    resource_attributes: typing.Optional[kubernetes.client.V1ResourceAttributes]
    def __init__(
        self,
        *,
        non_resource_attributes: typing.Optional[kubernetes.client.V1NonResourceAttributes] = ...,
        resource_attributes: typing.Optional[kubernetes.client.V1ResourceAttributes] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
