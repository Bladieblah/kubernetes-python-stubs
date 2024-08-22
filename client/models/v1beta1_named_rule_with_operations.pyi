import typing

class V1beta1NamedRuleWithOperations:
    api_groups: typing.Optional[list[str]]
    api_versions: typing.Optional[list[str]]
    operations: typing.Optional[list[str]]
    resource_names: typing.Optional[list[str]]
    resources: typing.Optional[list[str]]
    scope: typing.Optional[str]
    def __init__(
        self,
        *,
        api_groups: typing.Optional[list[str]] = ...,
        api_versions: typing.Optional[list[str]] = ...,
        operations: typing.Optional[list[str]] = ...,
        resource_names: typing.Optional[list[str]] = ...,
        resources: typing.Optional[list[str]] = ...,
        scope: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
