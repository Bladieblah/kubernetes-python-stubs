import typing

import kubernetes.client

class V1alpha1ValidatingAdmissionPolicyStatus:
    conditions: typing.Optional[list[kubernetes.client.V1Condition]]
    observed_generation: typing.Optional[int]
    type_checking: typing.Optional[kubernetes.client.V1alpha1TypeChecking]
    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes.client.V1Condition]] = ...,
        observed_generation: typing.Optional[int] = ...,
        type_checking: typing.Optional[kubernetes.client.V1alpha1TypeChecking] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
