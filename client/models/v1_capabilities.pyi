import typing
from urllib3 import BaseHTTPResponse

class V1Capabilities:
    add: typing.Optional[list[str]]
    drop: typing.Optional[list[str]]
    def __init__(self, *, add: typing.Optional[list[str]] = ..., drop: typing.Optional[list[str]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
