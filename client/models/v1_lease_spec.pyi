import datetime
import typing

class V1LeaseSpec:
    acquire_time: typing.Optional[datetime.datetime]
    holder_identity: typing.Optional[str]
    lease_duration_seconds: typing.Optional[int]
    lease_transitions: typing.Optional[int]
    renew_time: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        acquire_time: typing.Optional[datetime.datetime] = ...,
        holder_identity: typing.Optional[str] = ...,
        lease_duration_seconds: typing.Optional[int] = ...,
        lease_transitions: typing.Optional[int] = ...,
        renew_time: typing.Optional[datetime.datetime] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
