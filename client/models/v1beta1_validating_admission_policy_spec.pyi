import typing

import kubernetes.client

class V1beta1ValidatingAdmissionPolicySpec:
    audit_annotations: typing.Optional[list[kubernetes.client.V1beta1AuditAnnotation]]
    failure_policy: typing.Optional[str]
    match_conditions: typing.Optional[list[kubernetes.client.V1beta1MatchCondition]]
    match_constraints: typing.Optional[kubernetes.client.V1beta1MatchResources]
    param_kind: typing.Optional[kubernetes.client.V1beta1ParamKind]
    validations: typing.Optional[list[kubernetes.client.V1beta1Validation]]
    variables: typing.Optional[list[kubernetes.client.V1beta1Variable]]
    def __init__(
        self,
        *,
        audit_annotations: typing.Optional[list[kubernetes.client.V1beta1AuditAnnotation]] = ...,
        failure_policy: typing.Optional[str] = ...,
        match_conditions: typing.Optional[list[kubernetes.client.V1beta1MatchCondition]] = ...,
        match_constraints: typing.Optional[kubernetes.client.V1beta1MatchResources] = ...,
        param_kind: typing.Optional[kubernetes.client.V1beta1ParamKind] = ...,
        validations: typing.Optional[list[kubernetes.client.V1beta1Validation]] = ...,
        variables: typing.Optional[list[kubernetes.client.V1beta1Variable]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
