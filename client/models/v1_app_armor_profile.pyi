import typing

class V1AppArmorProfile:
    localhost_profile: typing.Optional[str]
    type: str
    def __init__(self, *, localhost_profile: typing.Optional[str] = ..., type: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
