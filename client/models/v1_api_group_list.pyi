import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1APIGroupList:
    api_version: typing.Optional[str]
    groups: list[kubernetes.client.V1APIGroup]
    kind: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        groups: list[kubernetes.client.V1APIGroup],
        kind: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
