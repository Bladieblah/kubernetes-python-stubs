import typing

class V1SubjectAccessReviewStatus:
    allowed: bool
    denied: typing.Optional[bool]
    evaluation_error: typing.Optional[str]
    reason: typing.Optional[str]
    def __init__(
        self,
        *,
        allowed: bool,
        denied: typing.Optional[bool] = ...,
        evaluation_error: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
