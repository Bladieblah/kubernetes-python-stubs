import typing

class ApiregistrationV1ServiceReference:
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    port: typing.Optional[int]
    def __init__(
        self,
        *,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        port: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
