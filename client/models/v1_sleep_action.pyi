import typing
from urllib3 import BaseHTTPResponse

class V1SleepAction:
    seconds: int
    def __init__(self, *, seconds: int) -> None: ...
    def to_dict(self) -> typing.Any: ...
