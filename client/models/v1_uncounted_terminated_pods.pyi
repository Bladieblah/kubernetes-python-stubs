import typing
from urllib3 import BaseHTTPResponse

class V1UncountedTerminatedPods:
    failed: typing.Optional[list[str]]
    succeeded: typing.Optional[list[str]]
    def __init__(
        self, *, failed: typing.Optional[list[str]] = ..., succeeded: typing.Optional[list[str]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
