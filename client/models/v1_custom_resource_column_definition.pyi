import typing
from urllib3 import BaseHTTPResponse

class V1CustomResourceColumnDefinition:
    description: typing.Optional[str]
    format: typing.Optional[str]
    json_path: str
    name: str
    priority: typing.Optional[int]
    type: str
    def __init__(
        self,
        *,
        description: typing.Optional[str] = ...,
        format: typing.Optional[str] = ...,
        json_path: str,
        name: str,
        priority: typing.Optional[int] = ...,
        type: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
