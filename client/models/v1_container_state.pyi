import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ContainerState:
    running: typing.Optional[kubernetes.client.V1ContainerStateRunning]
    terminated: typing.Optional[kubernetes.client.V1ContainerStateTerminated]
    waiting: typing.Optional[kubernetes.client.V1ContainerStateWaiting]
    def __init__(
        self,
        *,
        running: typing.Optional[kubernetes.client.V1ContainerStateRunning] = ...,
        terminated: typing.Optional[kubernetes.client.V1ContainerStateTerminated] = ...,
        waiting: typing.Optional[kubernetes.client.V1ContainerStateWaiting] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
