import typing
from urllib3 import BaseHTTPResponse

class V1beta3ResourcePolicyRule:
    api_groups: list[str]
    cluster_scope: typing.Optional[bool]
    namespaces: typing.Optional[list[str]]
    resources: list[str]
    verbs: list[str]
    def __init__(
        self,
        *,
        api_groups: list[str],
        cluster_scope: typing.Optional[bool] = ...,
        namespaces: typing.Optional[list[str]] = ...,
        resources: list[str],
        verbs: list[str],
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
