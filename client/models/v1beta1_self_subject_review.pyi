import typing

import kubernetes.client

class V1beta1SelfSubjectReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    status: typing.Optional[kubernetes.client.V1beta1SelfSubjectReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        status: typing.Optional[kubernetes.client.V1beta1SelfSubjectReviewStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
