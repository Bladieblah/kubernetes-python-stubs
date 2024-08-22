import typing

class V1NFSVolumeSource:
    path: str
    read_only: typing.Optional[bool]
    server: str
    def __init__(self, *, path: str, read_only: typing.Optional[bool] = ..., server: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
