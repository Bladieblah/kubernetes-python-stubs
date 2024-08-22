import typing
from urllib3 import BaseHTTPResponse

class V1CustomResourceDefinitionNames:
    categories: typing.Optional[list[str]]
    kind: str
    list_kind: typing.Optional[str]
    plural: str
    short_names: typing.Optional[list[str]]
    singular: typing.Optional[str]
    def __init__(
        self,
        *,
        categories: typing.Optional[list[str]] = ...,
        kind: str,
        list_kind: typing.Optional[str] = ...,
        plural: str,
        short_names: typing.Optional[list[str]] = ...,
        singular: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
