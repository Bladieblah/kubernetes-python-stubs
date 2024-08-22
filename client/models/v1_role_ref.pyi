import typing

class V1RoleRef:
    api_group: str
    kind: str
    name: str
    def __init__(self, *, api_group: str, kind: str, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
