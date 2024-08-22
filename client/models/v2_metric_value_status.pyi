import typing
from urllib3 import BaseHTTPResponse

class V2MetricValueStatus:
    average_utilization: typing.Optional[int]
    average_value: typing.Optional[str]
    value: typing.Optional[str]
    def __init__(
        self,
        *,
        average_utilization: typing.Optional[int] = ...,
        average_value: typing.Optional[str] = ...,
        value: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
