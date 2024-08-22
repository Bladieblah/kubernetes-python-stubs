import typing

class V1beta1Validation:
    expression: str
    message: typing.Optional[str]
    message_expression: typing.Optional[str]
    reason: typing.Optional[str]
    def __init__(
        self,
        *,
        expression: str,
        message: typing.Optional[str] = ...,
        message_expression: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
