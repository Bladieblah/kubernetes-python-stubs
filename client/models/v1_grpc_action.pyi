import typing

class V1GRPCAction:
    port: int
    service: typing.Optional[str]
    def __init__(self, *, port: int, service: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
