import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1PolicyRulesWithSubjects:
    non_resource_rules: typing.Optional[list[kubernetes.client.V1NonResourcePolicyRule]]
    resource_rules: typing.Optional[list[kubernetes.client.V1ResourcePolicyRule]]
    subjects: list[kubernetes.client.FlowcontrolV1Subject]
    def __init__(
        self,
        *,
        non_resource_rules: typing.Optional[list[kubernetes.client.V1NonResourcePolicyRule]] = ...,
        resource_rules: typing.Optional[list[kubernetes.client.V1ResourcePolicyRule]] = ...,
        subjects: list[kubernetes.client.FlowcontrolV1Subject],
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
