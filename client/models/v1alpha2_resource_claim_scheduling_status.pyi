import typing
from urllib3 import BaseHTTPResponse

class V1alpha2ResourceClaimSchedulingStatus:
    name: typing.Optional[str]
    unsuitable_nodes: typing.Optional[list[str]]
    def __init__(
        self, *, name: typing.Optional[str] = ..., unsuitable_nodes: typing.Optional[list[str]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
