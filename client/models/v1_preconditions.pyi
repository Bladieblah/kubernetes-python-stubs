import typing
from urllib3 import BaseHTTPResponse

class V1Preconditions:
    resource_version: typing.Optional[str]
    uid: typing.Optional[str]
    def __init__(self, *, resource_version: typing.Optional[str] = ..., uid: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
