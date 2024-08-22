import typing
from urllib3 import BaseHTTPResponse

class V1alpha1GroupVersionResource:
    group: typing.Optional[str]
    resource: typing.Optional[str]
    version: typing.Optional[str]
    def __init__(
        self,
        *,
        group: typing.Optional[str] = ...,
        resource: typing.Optional[str] = ...,
        version: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
