import typing

class V1ExpressionWarning:
    field_ref: str
    warning: str
    def __init__(self, *, field_ref: str, warning: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
