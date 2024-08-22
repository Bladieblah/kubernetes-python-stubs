import typing
from urllib3 import BaseHTTPResponse

class V1PodReadinessGate:
    condition_type: str
    def __init__(self, *, condition_type: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
