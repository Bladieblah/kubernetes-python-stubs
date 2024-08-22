import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1SuccessPolicy:
    rules: list[kubernetes.client.V1SuccessPolicyRule]
    def __init__(self, *, rules: list[kubernetes.client.V1SuccessPolicyRule]) -> None: ...
    def to_dict(self) -> typing.Any: ...
