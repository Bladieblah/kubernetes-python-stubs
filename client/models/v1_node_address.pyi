import typing

class V1NodeAddress:
    address: str
    type: str
    def __init__(self, *, address: str, type: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
