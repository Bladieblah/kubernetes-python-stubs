import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1StatefulSetStatus:
    available_replicas: typing.Optional[int]
    collision_count: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes.client.V1StatefulSetCondition]]
    current_replicas: typing.Optional[int]
    current_revision: typing.Optional[str]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: int
    update_revision: typing.Optional[str]
    updated_replicas: typing.Optional[int]
    def __init__(
        self,
        *,
        available_replicas: typing.Optional[int] = ...,
        collision_count: typing.Optional[int] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1StatefulSetCondition]] = ...,
        current_replicas: typing.Optional[int] = ...,
        current_revision: typing.Optional[str] = ...,
        observed_generation: typing.Optional[int] = ...,
        ready_replicas: typing.Optional[int] = ...,
        replicas: int,
        update_revision: typing.Optional[str] = ...,
        updated_replicas: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
