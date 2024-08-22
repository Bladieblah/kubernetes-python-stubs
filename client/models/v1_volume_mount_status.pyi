import typing
from urllib3 import BaseHTTPResponse

class V1VolumeMountStatus:
    mount_path: str
    name: str
    read_only: typing.Optional[bool]
    recursive_read_only: typing.Optional[str]
    def __init__(
        self,
        *,
        mount_path: str,
        name: str,
        read_only: typing.Optional[bool] = ...,
        recursive_read_only: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
