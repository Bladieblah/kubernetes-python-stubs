import typing
from urllib3 import BaseHTTPResponse

class V1beta1Variable:
    expression: str
    name: str
    def __init__(self, *, expression: str, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
