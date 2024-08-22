import typing
from urllib3 import BaseHTTPResponse

class V1AzureFileVolumeSource:
    read_only: typing.Optional[bool]
    secret_name: str
    share_name: str
    def __init__(self, *, read_only: typing.Optional[bool] = ..., secret_name: str, share_name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
