import typing
from urllib3 import BaseHTTPResponse

class V1GitRepoVolumeSource:
    directory: typing.Optional[str]
    repository: str
    revision: typing.Optional[str]
    def __init__(
        self, *, directory: typing.Optional[str] = ..., repository: str, revision: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
