import typing

class V2CrossVersionObjectReference:
    api_version: typing.Optional[str]
    kind: str
    name: str
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: str, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
