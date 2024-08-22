import typing
from urllib3 import BaseHTTPResponse

class V1PolicyRule:
    api_groups: typing.Optional[list[str]]
    non_resource_ur_ls: typing.Optional[list[str]]
    resource_names: typing.Optional[list[str]]
    resources: typing.Optional[list[str]]
    verbs: list[str]
    def __init__(
        self,
        *,
        api_groups: typing.Optional[list[str]] = ...,
        non_resource_ur_ls: typing.Optional[list[str]] = ...,
        resource_names: typing.Optional[list[str]] = ...,
        resources: typing.Optional[list[str]] = ...,
        verbs: list[str],
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
