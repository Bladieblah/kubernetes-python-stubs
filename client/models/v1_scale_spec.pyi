import typing
from urllib3 import BaseHTTPResponse

class V1ScaleSpec:
    replicas: typing.Optional[int]
    def __init__(self, *, replicas: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
