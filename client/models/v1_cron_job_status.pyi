import datetime
import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CronJobStatus:
    active: typing.Optional[list[kubernetes.client.V1ObjectReference]]
    last_schedule_time: typing.Optional[datetime.datetime]
    last_successful_time: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        active: typing.Optional[list[kubernetes.client.V1ObjectReference]] = ...,
        last_schedule_time: typing.Optional[datetime.datetime] = ...,
        last_successful_time: typing.Optional[datetime.datetime] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
