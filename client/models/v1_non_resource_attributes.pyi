import typing
from urllib3 import BaseHTTPResponse

class V1NonResourceAttributes:
    path: typing.Optional[str]
    verb: typing.Optional[str]
    def __init__(self, *, path: typing.Optional[str] = ..., verb: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
