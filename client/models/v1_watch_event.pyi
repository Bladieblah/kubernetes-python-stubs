import typing
from urllib3 import BaseHTTPResponse

class V1WatchEvent:
    object: typing.Any
    type: str
    def __init__(self, *, object: typing.Any, type: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
