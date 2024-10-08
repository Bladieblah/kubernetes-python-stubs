import typing

import kubernetes.client

class V1ValidatingWebhook:
    admission_review_versions: list[str]
    client_config: kubernetes.client.AdmissionregistrationV1WebhookClientConfig
    failure_policy: typing.Optional[str]
    match_conditions: typing.Optional[list[kubernetes.client.V1MatchCondition]]
    match_policy: typing.Optional[str]
    name: str
    namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    object_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    rules: typing.Optional[list[kubernetes.client.V1RuleWithOperations]]
    side_effects: str
    timeout_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        admission_review_versions: list[str],
        client_config: kubernetes.client.AdmissionregistrationV1WebhookClientConfig,
        failure_policy: typing.Optional[str] = ...,
        match_conditions: typing.Optional[list[kubernetes.client.V1MatchCondition]] = ...,
        match_policy: typing.Optional[str] = ...,
        name: str,
        namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        object_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        rules: typing.Optional[list[kubernetes.client.V1RuleWithOperations]] = ...,
        side_effects: str,
        timeout_seconds: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
