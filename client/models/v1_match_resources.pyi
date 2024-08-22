import typing

import kubernetes.client

class V1MatchResources:
    exclude_resource_rules: typing.Optional[list[kubernetes.client.V1NamedRuleWithOperations]]
    match_policy: typing.Optional[str]
    namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    object_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    resource_rules: typing.Optional[list[kubernetes.client.V1NamedRuleWithOperations]]
    def __init__(
        self,
        *,
        exclude_resource_rules: typing.Optional[list[kubernetes.client.V1NamedRuleWithOperations]] = ...,
        match_policy: typing.Optional[str] = ...,
        namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        object_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        resource_rules: typing.Optional[list[kubernetes.client.V1NamedRuleWithOperations]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
