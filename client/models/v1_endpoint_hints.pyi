import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1EndpointHints:
    for_zones: typing.Optional[list[kubernetes.client.V1ForZone]]
    def __init__(self, *, for_zones: typing.Optional[list[kubernetes.client.V1ForZone]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
