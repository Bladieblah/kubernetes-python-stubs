import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1TypeChecking:
    expression_warnings: typing.Optional[list[kubernetes.client.V1ExpressionWarning]]
    def __init__(
        self, *, expression_warnings: typing.Optional[list[kubernetes.client.V1ExpressionWarning]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
