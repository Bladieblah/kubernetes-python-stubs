import typing

import kubernetes.client

class V1SelfSubjectRulesReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1SelfSubjectRulesReviewSpec
    status: typing.Optional[kubernetes.client.V1SubjectRulesReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1SelfSubjectRulesReviewSpec,
        status: typing.Optional[kubernetes.client.V1SubjectRulesReviewStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
