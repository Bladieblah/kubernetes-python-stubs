import typing
from urllib3 import BaseHTTPResponse

class V1ScaleStatus:
    replicas: int
    selector: typing.Optional[str]
    def __init__(self, *, replicas: int, selector: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
