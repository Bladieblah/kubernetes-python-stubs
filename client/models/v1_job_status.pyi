import datetime
import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1JobStatus:
    active: typing.Optional[int]
    completed_indexes: typing.Optional[str]
    completion_time: typing.Optional[datetime.datetime]
    conditions: typing.Optional[list[kubernetes.client.V1JobCondition]]
    failed: typing.Optional[int]
    failed_indexes: typing.Optional[str]
    ready: typing.Optional[int]
    start_time: typing.Optional[datetime.datetime]
    succeeded: typing.Optional[int]
    terminating: typing.Optional[int]
    uncounted_terminated_pods: typing.Optional[kubernetes.client.V1UncountedTerminatedPods]
    def __init__(
        self,
        *,
        active: typing.Optional[int] = ...,
        completed_indexes: typing.Optional[str] = ...,
        completion_time: typing.Optional[datetime.datetime] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1JobCondition]] = ...,
        failed: typing.Optional[int] = ...,
        failed_indexes: typing.Optional[str] = ...,
        ready: typing.Optional[int] = ...,
        start_time: typing.Optional[datetime.datetime] = ...,
        succeeded: typing.Optional[int] = ...,
        terminating: typing.Optional[int] = ...,
        uncounted_terminated_pods: typing.Optional[kubernetes.client.V1UncountedTerminatedPods] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
