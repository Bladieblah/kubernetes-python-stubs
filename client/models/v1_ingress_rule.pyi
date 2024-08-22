import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1IngressRule:
    host: typing.Optional[str]
    http: typing.Optional[kubernetes.client.V1HTTPIngressRuleValue]
    def __init__(
        self, *, host: typing.Optional[str] = ..., http: typing.Optional[kubernetes.client.V1HTTPIngressRuleValue] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
