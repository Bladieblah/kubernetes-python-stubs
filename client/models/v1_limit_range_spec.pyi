import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1LimitRangeSpec:
    limits: list[kubernetes.client.V1LimitRangeItem]
    def __init__(self, *, limits: list[kubernetes.client.V1LimitRangeItem]) -> None: ...
    def to_dict(self) -> typing.Any: ...
