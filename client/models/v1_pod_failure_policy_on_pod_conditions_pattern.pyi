import typing
from urllib3 import BaseHTTPResponse

class V1PodFailurePolicyOnPodConditionsPattern:
    status: str
    type: str
    def __init__(self, *, status: str, type: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
