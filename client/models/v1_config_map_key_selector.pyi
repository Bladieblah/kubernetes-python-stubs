import typing

class V1ConfigMapKeySelector:
    key: str
    name: typing.Optional[str]
    optional: typing.Optional[bool]
    def __init__(
        self, *, key: str, name: typing.Optional[str] = ..., optional: typing.Optional[bool] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
