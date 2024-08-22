import typing

class V1CrossVersionObjectReference:
    api_version: typing.Optional[str]
    kind: str
    name: str
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: str, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
