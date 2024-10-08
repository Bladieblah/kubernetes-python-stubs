import typing

import kubernetes.client

class V1alpha1TypeChecking:
    expression_warnings: typing.Optional[list[kubernetes.client.V1alpha1ExpressionWarning]]
    def __init__(
        self, *, expression_warnings: typing.Optional[list[kubernetes.client.V1alpha1ExpressionWarning]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
