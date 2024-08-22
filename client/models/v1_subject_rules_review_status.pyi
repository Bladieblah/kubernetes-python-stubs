import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1SubjectRulesReviewStatus:
    evaluation_error: typing.Optional[str]
    incomplete: bool
    non_resource_rules: list[kubernetes.client.V1NonResourceRule]
    resource_rules: list[kubernetes.client.V1ResourceRule]
    def __init__(
        self,
        *,
        evaluation_error: typing.Optional[str] = ...,
        incomplete: bool,
        non_resource_rules: list[kubernetes.client.V1NonResourceRule],
        resource_rules: list[kubernetes.client.V1ResourceRule],
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
