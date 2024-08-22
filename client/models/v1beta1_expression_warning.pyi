import typing
from urllib3 import BaseHTTPResponse

class V1beta1ExpressionWarning:
    field_ref: str
    warning: str
    def __init__(self, *, field_ref: str, warning: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
