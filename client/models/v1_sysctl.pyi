import typing
from urllib3 import BaseHTTPResponse

class V1Sysctl:
    name: str
    value: str
    def __init__(self, *, name: str, value: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
