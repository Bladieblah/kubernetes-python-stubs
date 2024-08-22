import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha2ResourceHandle:
    data: typing.Optional[str]
    driver_name: typing.Optional[str]
    structured_data: typing.Optional[kubernetes.client.V1alpha2StructuredResourceHandle]
    def __init__(
        self,
        *,
        data: typing.Optional[str] = ...,
        driver_name: typing.Optional[str] = ...,
        structured_data: typing.Optional[kubernetes.client.V1alpha2StructuredResourceHandle] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
