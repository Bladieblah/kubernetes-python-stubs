import datetime
import typing

import kubernetes.client

class V1PodDisruptionBudgetStatus:
    conditions: typing.Optional[list[kubernetes.client.V1Condition]]
    current_healthy: int
    desired_healthy: int
    disrupted_pods: typing.Optional[dict[str, datetime.datetime]]
    disruptions_allowed: int
    expected_pods: int
    observed_generation: typing.Optional[int]
    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes.client.V1Condition]] = ...,
        current_healthy: int,
        desired_healthy: int,
        disrupted_pods: typing.Optional[dict[str, datetime.datetime]] = ...,
        disruptions_allowed: int,
        expected_pods: int,
        observed_generation: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
