import typing
from urllib3 import BaseHTTPResponse

class V1UserInfo:
    extra: typing.Optional[dict[str, list[str]]]
    groups: typing.Optional[list[str]]
    uid: typing.Optional[str]
    username: typing.Optional[str]
    def __init__(
        self,
        *,
        extra: typing.Optional[dict[str, list[str]]] = ...,
        groups: typing.Optional[list[str]] = ...,
        uid: typing.Optional[str] = ...,
        username: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
