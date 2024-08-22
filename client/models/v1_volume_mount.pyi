import typing
from urllib3 import BaseHTTPResponse

class V1VolumeMount:
    mount_path: str
    mount_propagation: typing.Optional[str]
    name: str
    read_only: typing.Optional[bool]
    recursive_read_only: typing.Optional[str]
    sub_path: typing.Optional[str]
    sub_path_expr: typing.Optional[str]
    def __init__(
        self,
        *,
        mount_path: str,
        mount_propagation: typing.Optional[str] = ...,
        name: str,
        read_only: typing.Optional[bool] = ...,
        recursive_read_only: typing.Optional[str] = ...,
        sub_path: typing.Optional[str] = ...,
        sub_path_expr: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
