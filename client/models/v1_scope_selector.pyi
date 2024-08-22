import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ScopeSelector:
    match_expressions: typing.Optional[list[kubernetes.client.V1ScopedResourceSelectorRequirement]]
    def __init__(
        self, *, match_expressions: typing.Optional[list[kubernetes.client.V1ScopedResourceSelectorRequirement]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
