import datetime
import typing
from urllib3 import BaseHTTPResponse

class V1ContainerStateTerminated:
    container_id: typing.Optional[str]
    exit_code: int
    finished_at: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    signal: typing.Optional[int]
    started_at: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        container_id: typing.Optional[str] = ...,
        exit_code: int,
        finished_at: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        signal: typing.Optional[int] = ...,
        started_at: typing.Optional[datetime.datetime] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
