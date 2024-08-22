import datetime
import typing

import kubernetes.client

class V2HorizontalPodAutoscalerStatus:
    conditions: typing.Optional[list[kubernetes.client.V2HorizontalPodAutoscalerCondition]]
    current_metrics: typing.Optional[list[kubernetes.client.V2MetricStatus]]
    current_replicas: typing.Optional[int]
    desired_replicas: int
    last_scale_time: typing.Optional[datetime.datetime]
    observed_generation: typing.Optional[int]
    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes.client.V2HorizontalPodAutoscalerCondition]] = ...,
        current_metrics: typing.Optional[list[kubernetes.client.V2MetricStatus]] = ...,
        current_replicas: typing.Optional[int] = ...,
        desired_replicas: int,
        last_scale_time: typing.Optional[datetime.datetime] = ...,
        observed_generation: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
