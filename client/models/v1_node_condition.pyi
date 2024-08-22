import datetime
import typing
from urllib3 import BaseHTTPResponse

class V1NodeCondition:
    last_heartbeat_time: typing.Optional[datetime.datetime]
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
    def __init__(
        self,
        *,
        last_heartbeat_time: typing.Optional[datetime.datetime] = ...,
        last_transition_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        status: str,
        type: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
