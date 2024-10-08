import typing

import kubernetes.client

class V1SelfSubjectReviewStatus:
    user_info: typing.Optional[kubernetes.client.V1UserInfo]
    def __init__(self, *, user_info: typing.Optional[kubernetes.client.V1UserInfo] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
