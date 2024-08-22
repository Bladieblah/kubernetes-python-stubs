import datetime
import typing
from urllib3 import BaseHTTPResponse

class CoreV1EventSeries:
    count: typing.Optional[int]
    last_observed_time: typing.Optional[datetime.datetime]
    def __init__(
        self, *, count: typing.Optional[int] = ..., last_observed_time: typing.Optional[datetime.datetime] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
