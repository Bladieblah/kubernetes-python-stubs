import typing

class V1ExternalDocumentation:
    description: typing.Optional[str]
    url: typing.Optional[str]
    def __init__(self, *, description: typing.Optional[str] = ..., url: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
