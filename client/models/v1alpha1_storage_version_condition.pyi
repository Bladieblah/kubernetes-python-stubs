import datetime
import typing
from urllib3 import BaseHTTPResponse

class V1alpha1StorageVersionCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    message: str
    observed_generation: typing.Optional[int]
    reason: str
    status: str
    type: str
    def __init__(
        self,
        *,
        last_transition_time: typing.Optional[datetime.datetime] = ...,
        message: str,
        observed_generation: typing.Optional[int] = ...,
        reason: str,
        status: str,
        type: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
