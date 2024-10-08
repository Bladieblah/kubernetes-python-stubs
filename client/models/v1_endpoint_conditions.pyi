import typing

class V1EndpointConditions:
    ready: typing.Optional[bool]
    serving: typing.Optional[bool]
    terminating: typing.Optional[bool]
    def __init__(
        self,
        *,
        ready: typing.Optional[bool] = ...,
        serving: typing.Optional[bool] = ...,
        terminating: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
