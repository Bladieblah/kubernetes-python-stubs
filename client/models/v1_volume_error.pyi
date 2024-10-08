import datetime
import typing

class V1VolumeError:
    message: typing.Optional[str]
    time: typing.Optional[datetime.datetime]
    def __init__(
        self, *, message: typing.Optional[str] = ..., time: typing.Optional[datetime.datetime] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
