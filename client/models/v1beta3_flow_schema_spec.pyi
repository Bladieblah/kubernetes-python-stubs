import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1beta3FlowSchemaSpec:
    distinguisher_method: typing.Optional[kubernetes.client.V1beta3FlowDistinguisherMethod]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: kubernetes.client.V1beta3PriorityLevelConfigurationReference
    rules: typing.Optional[list[kubernetes.client.V1beta3PolicyRulesWithSubjects]]
    def __init__(
        self,
        *,
        distinguisher_method: typing.Optional[kubernetes.client.V1beta3FlowDistinguisherMethod] = ...,
        matching_precedence: typing.Optional[int] = ...,
        priority_level_configuration: kubernetes.client.V1beta3PriorityLevelConfigurationReference,
        rules: typing.Optional[list[kubernetes.client.V1beta3PolicyRulesWithSubjects]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
