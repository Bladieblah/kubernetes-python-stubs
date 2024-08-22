import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1EndpointSubset:
    addresses: typing.Optional[list[kubernetes.client.V1EndpointAddress]]
    not_ready_addresses: typing.Optional[list[kubernetes.client.V1EndpointAddress]]
    ports: typing.Optional[list[kubernetes.client.CoreV1EndpointPort]]
    def __init__(
        self,
        *,
        addresses: typing.Optional[list[kubernetes.client.V1EndpointAddress]] = ...,
        not_ready_addresses: typing.Optional[list[kubernetes.client.V1EndpointAddress]] = ...,
        ports: typing.Optional[list[kubernetes.client.CoreV1EndpointPort]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
