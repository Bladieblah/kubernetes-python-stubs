import datetime
import typing

class V1PersistentVolumeClaimCondition:
    last_probe_time: typing.Optional[datetime.datetime]
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
    def __init__(
        self,
        *,
        last_probe_time: typing.Optional[datetime.datetime] = ...,
        last_transition_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        status: str,
        type: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
