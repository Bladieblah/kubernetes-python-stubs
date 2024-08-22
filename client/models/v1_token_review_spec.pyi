import typing
from urllib3 import BaseHTTPResponse

class V1TokenReviewSpec:
    audiences: typing.Optional[list[str]]
    token: typing.Optional[str]
    def __init__(self, *, audiences: typing.Optional[list[str]] = ..., token: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
