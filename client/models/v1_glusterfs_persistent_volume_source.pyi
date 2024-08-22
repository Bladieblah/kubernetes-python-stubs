import typing
from urllib3 import BaseHTTPResponse

class V1GlusterfsPersistentVolumeSource:
    endpoints: str
    endpoints_namespace: typing.Optional[str]
    path: str
    read_only: typing.Optional[bool]
    def __init__(
        self,
        *,
        endpoints: str,
        endpoints_namespace: typing.Optional[str] = ...,
        path: str,
        read_only: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
