import datetime
import typing
from urllib3 import BaseHTTPResponse

class EventsV1EventSeries:
    count: int
    last_observed_time: datetime.datetime
    def __init__(self, *, count: int, last_observed_time: datetime.datetime) -> None: ...
    def to_dict(self) -> typing.Any: ...
