import typing

class V1TypedObjectReference:
    api_group: typing.Optional[str]
    kind: str
    name: str
    namespace: typing.Optional[str]
    def __init__(
        self, *, api_group: typing.Optional[str] = ..., kind: str, name: str, namespace: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
