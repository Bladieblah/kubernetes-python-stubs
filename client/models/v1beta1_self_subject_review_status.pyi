import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1beta1SelfSubjectReviewStatus:
    user_info: typing.Optional[kubernetes.client.V1UserInfo]
    def __init__(self, *, user_info: typing.Optional[kubernetes.client.V1UserInfo] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
