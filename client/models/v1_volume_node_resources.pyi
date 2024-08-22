import typing
from urllib3 import BaseHTTPResponse

class V1VolumeNodeResources:
    count: typing.Optional[int]
    def __init__(self, *, count: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
