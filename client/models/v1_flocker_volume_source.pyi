import typing
from urllib3 import BaseHTTPResponse

class V1FlockerVolumeSource:
    dataset_name: typing.Optional[str]
    dataset_uuid: typing.Optional[str]
    def __init__(
        self, *, dataset_name: typing.Optional[str] = ..., dataset_uuid: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
