import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1TopologySelectorTerm:
    match_label_expressions: typing.Optional[list[kubernetes.client.V1TopologySelectorLabelRequirement]]
    def __init__(
        self,
        *,
        match_label_expressions: typing.Optional[list[kubernetes.client.V1TopologySelectorLabelRequirement]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
