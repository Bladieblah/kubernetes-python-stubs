import typing
from urllib3 import BaseHTTPResponse

class CoreV1EndpointPort:
    app_protocol: typing.Optional[str]
    name: typing.Optional[str]
    port: int
    protocol: typing.Optional[str]
    def __init__(
        self,
        *,
        app_protocol: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        port: int,
        protocol: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
