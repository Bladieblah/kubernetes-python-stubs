import typing

import kubernetes.client

class V1beta1TypeChecking:
    expression_warnings: typing.Optional[list[kubernetes.client.V1beta1ExpressionWarning]]
    def __init__(
        self, *, expression_warnings: typing.Optional[list[kubernetes.client.V1beta1ExpressionWarning]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
