import typing

class V1ContainerStateWaiting:
    message: typing.Optional[str]
    reason: typing.Optional[str]
    def __init__(self, *, message: typing.Optional[str] = ..., reason: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
