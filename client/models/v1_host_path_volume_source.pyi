import typing

class V1HostPathVolumeSource:
    path: str
    type: typing.Optional[str]
    def __init__(self, *, path: str, type: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
