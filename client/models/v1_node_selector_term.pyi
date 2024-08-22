import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1NodeSelectorTerm:
    match_expressions: typing.Optional[list[kubernetes.client.V1NodeSelectorRequirement]]
    match_fields: typing.Optional[list[kubernetes.client.V1NodeSelectorRequirement]]
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[list[kubernetes.client.V1NodeSelectorRequirement]] = ...,
        match_fields: typing.Optional[list[kubernetes.client.V1NodeSelectorRequirement]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
