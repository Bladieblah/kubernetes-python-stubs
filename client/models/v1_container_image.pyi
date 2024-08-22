import typing
from urllib3 import BaseHTTPResponse

class V1ContainerImage:
    names: typing.Optional[list[str]]
    size_bytes: typing.Optional[int]
    def __init__(self, *, names: typing.Optional[list[str]] = ..., size_bytes: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
