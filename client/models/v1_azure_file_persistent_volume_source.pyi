import typing
from urllib3 import BaseHTTPResponse

class V1AzureFilePersistentVolumeSource:
    read_only: typing.Optional[bool]
    secret_name: str
    secret_namespace: typing.Optional[str]
    share_name: str
    def __init__(
        self,
        *,
        read_only: typing.Optional[bool] = ...,
        secret_name: str,
        secret_namespace: typing.Optional[str] = ...,
        share_name: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
