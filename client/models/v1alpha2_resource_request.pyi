import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha2ResourceRequest:
    named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesRequest]
    vendor_parameters: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesRequest] = ...,
        vendor_parameters: typing.Optional[typing.Any] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
