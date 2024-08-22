import typing
from urllib3 import BaseHTTPResponse

class V1ContainerPort:
    container_port: int
    host_ip: typing.Optional[str]
    host_port: typing.Optional[int]
    name: typing.Optional[str]
    protocol: typing.Optional[str]
    def __init__(
        self,
        *,
        container_port: int,
        host_ip: typing.Optional[str] = ...,
        host_port: typing.Optional[int] = ...,
        name: typing.Optional[str] = ...,
        protocol: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
