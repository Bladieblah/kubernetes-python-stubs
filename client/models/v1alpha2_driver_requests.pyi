import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha2DriverRequests:
    driver_name: typing.Optional[str]
    requests: typing.Optional[list[kubernetes.client.V1alpha2ResourceRequest]]
    vendor_parameters: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        driver_name: typing.Optional[str] = ...,
        requests: typing.Optional[list[kubernetes.client.V1alpha2ResourceRequest]] = ...,
        vendor_parameters: typing.Optional[typing.Any] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
