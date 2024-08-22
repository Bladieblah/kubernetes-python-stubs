import typing
from urllib3 import BaseHTTPResponse

class V1StatefulSetOrdinals:
    start: typing.Optional[int]
    def __init__(self, *, start: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
