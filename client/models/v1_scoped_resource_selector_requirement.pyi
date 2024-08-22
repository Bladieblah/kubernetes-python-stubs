import typing
from urllib3 import BaseHTTPResponse

class V1ScopedResourceSelectorRequirement:
    operator: str
    scope_name: str
    values: typing.Optional[list[str]]
    def __init__(self, *, operator: str, scope_name: str, values: typing.Optional[list[str]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
