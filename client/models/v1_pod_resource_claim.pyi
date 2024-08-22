import typing

import kubernetes.client

class V1PodResourceClaim:
    name: str
    source: typing.Optional[kubernetes.client.V1ClaimSource]
    def __init__(self, *, name: str, source: typing.Optional[kubernetes.client.V1ClaimSource] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
