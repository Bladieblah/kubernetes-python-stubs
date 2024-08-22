import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha2ResourceFilter:
    driver_name: typing.Optional[str]
    named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesFilter]
    def __init__(
        self,
        *,
        driver_name: typing.Optional[str] = ...,
        named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesFilter] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
