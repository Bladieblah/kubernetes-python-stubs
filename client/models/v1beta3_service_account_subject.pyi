import typing

class V1beta3ServiceAccountSubject:
    name: str
    namespace: str
    def __init__(self, *, name: str, namespace: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
