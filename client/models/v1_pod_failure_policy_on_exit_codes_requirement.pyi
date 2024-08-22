import typing
from urllib3 import BaseHTTPResponse

class V1PodFailurePolicyOnExitCodesRequirement:
    container_name: typing.Optional[str]
    operator: str
    values: list[int]
    def __init__(self, *, container_name: typing.Optional[str] = ..., operator: str, values: list[int]) -> None: ...
    def to_dict(self) -> typing.Any: ...
