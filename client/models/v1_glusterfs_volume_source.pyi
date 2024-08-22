import typing

class V1GlusterfsVolumeSource:
    endpoints: str
    path: str
    read_only: typing.Optional[bool]
    def __init__(self, *, endpoints: str, path: str, read_only: typing.Optional[bool] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
