import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CustomResourceDefinitionStatus:
    accepted_names: typing.Optional[kubernetes.client.V1CustomResourceDefinitionNames]
    conditions: typing.Optional[list[kubernetes.client.V1CustomResourceDefinitionCondition]]
    stored_versions: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        accepted_names: typing.Optional[kubernetes.client.V1CustomResourceDefinitionNames] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1CustomResourceDefinitionCondition]] = ...,
        stored_versions: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
