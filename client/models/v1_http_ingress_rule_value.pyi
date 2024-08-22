import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1HTTPIngressRuleValue:
    paths: list[kubernetes.client.V1HTTPIngressPath]
    def __init__(self, *, paths: list[kubernetes.client.V1HTTPIngressPath]) -> None: ...
    def to_dict(self) -> typing.Any: ...
