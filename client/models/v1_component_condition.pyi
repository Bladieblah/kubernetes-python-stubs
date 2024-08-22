import typing
from urllib3 import BaseHTTPResponse

class V1ComponentCondition:
    error: typing.Optional[str]
    message: typing.Optional[str]
    status: str
    type: str
    def __init__(
        self, *, error: typing.Optional[str] = ..., message: typing.Optional[str] = ..., status: str, type: str
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
