import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha2DriverAllocationResult:
    named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesAllocationResult]
    vendor_request_parameters: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesAllocationResult] = ...,
        vendor_request_parameters: typing.Optional[typing.Any] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
