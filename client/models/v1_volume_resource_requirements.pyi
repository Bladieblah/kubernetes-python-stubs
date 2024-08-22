import typing
from urllib3 import BaseHTTPResponse

class V1VolumeResourceRequirements:
    limits: typing.Optional[dict[str, str]]
    requests: typing.Optional[dict[str, str]]
    def __init__(
        self, *, limits: typing.Optional[dict[str, str]] = ..., requests: typing.Optional[dict[str, str]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
