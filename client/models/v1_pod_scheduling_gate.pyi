import typing

class V1PodSchedulingGate:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
