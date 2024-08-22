import typing
from urllib3 import BaseHTTPResponse

class V1Overhead:
    pod_fixed: typing.Optional[dict[str, str]]
    def __init__(self, *, pod_fixed: typing.Optional[dict[str, str]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
