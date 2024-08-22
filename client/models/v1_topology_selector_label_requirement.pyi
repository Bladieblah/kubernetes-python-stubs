import typing
from urllib3 import BaseHTTPResponse

class V1TopologySelectorLabelRequirement:
    key: str
    values: list[str]
    def __init__(self, *, key: str, values: list[str]) -> None: ...
    def to_dict(self) -> typing.Any: ...
