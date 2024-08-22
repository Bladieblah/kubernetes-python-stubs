import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha1SelfSubjectReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    status: typing.Optional[kubernetes.client.V1alpha1SelfSubjectReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        status: typing.Optional[kubernetes.client.V1alpha1SelfSubjectReviewStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
