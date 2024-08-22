import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha2NamedResourcesInstance:
    attributes: typing.Optional[list[kubernetes.client.V1alpha2NamedResourcesAttribute]]
    name: str
    def __init__(
        self, *, attributes: typing.Optional[list[kubernetes.client.V1alpha2NamedResourcesAttribute]] = ..., name: str
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
