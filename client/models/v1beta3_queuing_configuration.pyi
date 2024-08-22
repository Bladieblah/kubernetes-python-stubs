import typing
from urllib3 import BaseHTTPResponse

class V1beta3QueuingConfiguration:
    hand_size: typing.Optional[int]
    queue_length_limit: typing.Optional[int]
    queues: typing.Optional[int]
    def __init__(
        self,
        *,
        hand_size: typing.Optional[int] = ...,
        queue_length_limit: typing.Optional[int] = ...,
        queues: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
