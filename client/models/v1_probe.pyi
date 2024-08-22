import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1Probe:
    _exec: typing.Optional[kubernetes.client.V1ExecAction]
    failure_threshold: typing.Optional[int]
    grpc: typing.Optional[kubernetes.client.V1GRPCAction]
    http_get: typing.Optional[kubernetes.client.V1HTTPGetAction]
    initial_delay_seconds: typing.Optional[int]
    period_seconds: typing.Optional[int]
    success_threshold: typing.Optional[int]
    tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction]
    termination_grace_period_seconds: typing.Optional[int]
    timeout_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        _exec: typing.Optional[kubernetes.client.V1ExecAction] = ...,
        failure_threshold: typing.Optional[int] = ...,
        grpc: typing.Optional[kubernetes.client.V1GRPCAction] = ...,
        http_get: typing.Optional[kubernetes.client.V1HTTPGetAction] = ...,
        initial_delay_seconds: typing.Optional[int] = ...,
        period_seconds: typing.Optional[int] = ...,
        success_threshold: typing.Optional[int] = ...,
        tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction] = ...,
        termination_grace_period_seconds: typing.Optional[int] = ...,
        timeout_seconds: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
