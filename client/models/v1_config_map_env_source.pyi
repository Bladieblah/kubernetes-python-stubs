import typing

class V1ConfigMapEnvSource:
    name: typing.Optional[str]
    optional: typing.Optional[bool]
    def __init__(self, *, name: typing.Optional[str] = ..., optional: typing.Optional[bool] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
