import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ReplicaSetStatus:
    available_replicas: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes.client.V1ReplicaSetCondition]]
    fully_labeled_replicas: typing.Optional[int]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: int
    def __init__(
        self,
        *,
        available_replicas: typing.Optional[int] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1ReplicaSetCondition]] = ...,
        fully_labeled_replicas: typing.Optional[int] = ...,
        observed_generation: typing.Optional[int] = ...,
        ready_replicas: typing.Optional[int] = ...,
        replicas: int,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
