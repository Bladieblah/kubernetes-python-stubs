import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha2StructuredResourceHandle:
    node_name: typing.Optional[str]
    results: list[kubernetes.client.V1alpha2DriverAllocationResult]
    vendor_claim_parameters: typing.Optional[typing.Any]
    vendor_class_parameters: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        node_name: typing.Optional[str] = ...,
        results: list[kubernetes.client.V1alpha2DriverAllocationResult],
        vendor_claim_parameters: typing.Optional[typing.Any] = ...,
        vendor_class_parameters: typing.Optional[typing.Any] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
