import typing
from urllib3 import BaseHTTPResponse

class V1ServicePort:
    app_protocol: typing.Optional[str]
    name: typing.Optional[str]
    node_port: typing.Optional[int]
    port: int
    protocol: typing.Optional[str]
    target_port: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        app_protocol: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        node_port: typing.Optional[int] = ...,
        port: int,
        protocol: typing.Optional[str] = ...,
        target_port: typing.Optional[typing.Any] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
