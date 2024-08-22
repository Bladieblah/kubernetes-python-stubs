import typing

class V1ResourceRule:
    api_groups: typing.Optional[list[str]]
    resource_names: typing.Optional[list[str]]
    resources: typing.Optional[list[str]]
    verbs: list[str]
    def __init__(
        self,
        *,
        api_groups: typing.Optional[list[str]] = ...,
        resource_names: typing.Optional[list[str]] = ...,
        resources: typing.Optional[list[str]] = ...,
        verbs: list[str],
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
