import typing

import kubernetes.client

class V1beta3PolicyRulesWithSubjects:
    non_resource_rules: typing.Optional[list[kubernetes.client.V1beta3NonResourcePolicyRule]]
    resource_rules: typing.Optional[list[kubernetes.client.V1beta3ResourcePolicyRule]]
    subjects: list[kubernetes.client.V1beta3Subject]
    def __init__(
        self,
        *,
        non_resource_rules: typing.Optional[list[kubernetes.client.V1beta3NonResourcePolicyRule]] = ...,
        resource_rules: typing.Optional[list[kubernetes.client.V1beta3ResourcePolicyRule]] = ...,
        subjects: list[kubernetes.client.V1beta3Subject],
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
