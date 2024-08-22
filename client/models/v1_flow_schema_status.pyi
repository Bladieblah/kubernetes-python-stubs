import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1FlowSchemaStatus:
    conditions: typing.Optional[list[kubernetes.client.V1FlowSchemaCondition]]
    def __init__(self, *, conditions: typing.Optional[list[kubernetes.client.V1FlowSchemaCondition]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
