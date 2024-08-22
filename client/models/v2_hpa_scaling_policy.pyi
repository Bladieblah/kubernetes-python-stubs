import typing

class V2HPAScalingPolicy:
    period_seconds: int
    type: str
    value: int
    def __init__(self, *, period_seconds: int, type: str, value: int) -> None: ...
    def to_dict(self) -> typing.Any: ...
