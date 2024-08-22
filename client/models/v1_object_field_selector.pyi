import typing
from urllib3 import BaseHTTPResponse

class V1ObjectFieldSelector:
    api_version: typing.Optional[str]
    field_path: str
    def __init__(self, *, api_version: typing.Optional[str] = ..., field_path: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
