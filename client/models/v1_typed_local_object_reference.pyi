import typing
from urllib3 import BaseHTTPResponse

class V1TypedLocalObjectReference:
    api_group: typing.Optional[str]
    kind: str
    name: str
    def __init__(self, *, api_group: typing.Optional[str] = ..., kind: str, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
