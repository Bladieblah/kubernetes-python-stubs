import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1APIServiceStatus:
    conditions: typing.Optional[list[kubernetes.client.V1APIServiceCondition]]
    def __init__(self, *, conditions: typing.Optional[list[kubernetes.client.V1APIServiceCondition]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
