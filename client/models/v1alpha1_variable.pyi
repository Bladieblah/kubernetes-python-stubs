import typing

class V1alpha1Variable:
    expression: str
    name: str
    def __init__(self, *, expression: str, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
