import typing
from urllib3 import BaseHTTPResponse

class V1LabelSelectorRequirement:
    key: str
    operator: str
    values: typing.Optional[list[str]]
    def __init__(self, *, key: str, operator: str, values: typing.Optional[list[str]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
