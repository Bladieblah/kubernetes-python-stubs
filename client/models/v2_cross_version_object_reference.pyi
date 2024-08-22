import typing
from urllib3 import BaseHTTPResponse

class V2CrossVersionObjectReference:
    api_version: typing.Optional[str]
    kind: str
    name: str
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: str, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
