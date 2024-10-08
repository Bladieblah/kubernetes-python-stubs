import typing

class V1alpha1ParentReference:
    group: typing.Optional[str]
    name: str
    namespace: typing.Optional[str]
    resource: str
    def __init__(
        self, *, group: typing.Optional[str] = ..., name: str, namespace: typing.Optional[str] = ..., resource: str
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
