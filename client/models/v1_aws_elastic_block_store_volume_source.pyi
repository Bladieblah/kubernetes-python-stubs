import typing
from urllib3 import BaseHTTPResponse

class V1AWSElasticBlockStoreVolumeSource:
    fs_type: typing.Optional[str]
    partition: typing.Optional[int]
    read_only: typing.Optional[bool]
    volume_id: str
    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        partition: typing.Optional[int] = ...,
        read_only: typing.Optional[bool] = ...,
        volume_id: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
