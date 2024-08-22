import typing

class V1alpha1AuditAnnotation:
    key: str
    value_expression: str
    def __init__(self, *, key: str, value_expression: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
