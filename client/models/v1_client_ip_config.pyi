import typing

class V1ClientIPConfig:
    timeout_seconds: typing.Optional[int]
    def __init__(self, *, timeout_seconds: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
