import datetime
import typing

class V1Condition:
    last_transition_time: datetime.datetime
    message: str
    observed_generation: typing.Optional[int]
    reason: str
    status: str
    type: str
    def __init__(
        self,
        *,
        last_transition_time: datetime.datetime,
        message: str,
        observed_generation: typing.Optional[int] = ...,
        reason: str,
        status: str,
        type: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
