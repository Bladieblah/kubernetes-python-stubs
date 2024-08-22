import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1FlowSchemaSpec:
    distinguisher_method: typing.Optional[kubernetes.client.V1FlowDistinguisherMethod]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: kubernetes.client.V1PriorityLevelConfigurationReference
    rules: typing.Optional[list[kubernetes.client.V1PolicyRulesWithSubjects]]
    def __init__(
        self,
        *,
        distinguisher_method: typing.Optional[kubernetes.client.V1FlowDistinguisherMethod] = ...,
        matching_precedence: typing.Optional[int] = ...,
        priority_level_configuration: kubernetes.client.V1PriorityLevelConfigurationReference,
        rules: typing.Optional[list[kubernetes.client.V1PolicyRulesWithSubjects]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
