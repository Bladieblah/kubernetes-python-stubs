import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha2NamedResourcesResources:
    instances: list[kubernetes.client.V1alpha2NamedResourcesInstance]
    def __init__(self, *, instances: list[kubernetes.client.V1alpha2NamedResourcesInstance]) -> None: ...
    def to_dict(self) -> typing.Any: ...
