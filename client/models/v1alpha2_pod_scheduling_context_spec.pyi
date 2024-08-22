import typing
from urllib3 import BaseHTTPResponse

class V1alpha2PodSchedulingContextSpec:
    potential_nodes: typing.Optional[list[str]]
    selected_node: typing.Optional[str]
    def __init__(
        self, *, potential_nodes: typing.Optional[list[str]] = ..., selected_node: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
