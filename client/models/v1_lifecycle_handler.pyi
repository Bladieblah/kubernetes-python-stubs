import typing

import kubernetes.client

class V1LifecycleHandler:
    _exec: typing.Optional[kubernetes.client.V1ExecAction]
    http_get: typing.Optional[kubernetes.client.V1HTTPGetAction]
    sleep: typing.Optional[kubernetes.client.V1SleepAction]
    tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction]
    def __init__(
        self,
        *,
        _exec: typing.Optional[kubernetes.client.V1ExecAction] = ...,
        http_get: typing.Optional[kubernetes.client.V1HTTPGetAction] = ...,
        sleep: typing.Optional[kubernetes.client.V1SleepAction] = ...,
        tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
