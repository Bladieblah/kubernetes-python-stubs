import typing

class V1EmptyDirVolumeSource:
    medium: typing.Optional[str]
    size_limit: typing.Optional[str]
    def __init__(self, *, medium: typing.Optional[str] = ..., size_limit: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
