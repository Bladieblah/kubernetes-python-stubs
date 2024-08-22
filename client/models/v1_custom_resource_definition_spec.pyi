import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CustomResourceDefinitionSpec:
    conversion: typing.Optional[kubernetes.client.V1CustomResourceConversion]
    group: str
    names: kubernetes.client.V1CustomResourceDefinitionNames
    preserve_unknown_fields: typing.Optional[bool]
    scope: str
    versions: list[kubernetes.client.V1CustomResourceDefinitionVersion]
    def __init__(
        self,
        *,
        conversion: typing.Optional[kubernetes.client.V1CustomResourceConversion] = ...,
        group: str,
        names: kubernetes.client.V1CustomResourceDefinitionNames,
        preserve_unknown_fields: typing.Optional[bool] = ...,
        scope: str,
        versions: list[kubernetes.client.V1CustomResourceDefinitionVersion],
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
