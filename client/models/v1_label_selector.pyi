import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1LabelSelector:
    match_expressions: typing.Optional[list[kubernetes.client.V1LabelSelectorRequirement]]
    match_labels: typing.Optional[dict[str, str]]
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[list[kubernetes.client.V1LabelSelectorRequirement]] = ...,
        match_labels: typing.Optional[dict[str, str]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
