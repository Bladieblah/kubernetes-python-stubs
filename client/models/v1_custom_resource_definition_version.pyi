import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CustomResourceDefinitionVersion:
    additional_printer_columns: typing.Optional[list[kubernetes.client.V1CustomResourceColumnDefinition]]
    deprecated: typing.Optional[bool]
    deprecation_warning: typing.Optional[str]
    name: str
    schema: typing.Optional[kubernetes.client.V1CustomResourceValidation]
    selectable_fields: typing.Optional[list[kubernetes.client.V1SelectableField]]
    served: bool
    storage: bool
    subresources: typing.Optional[kubernetes.client.V1CustomResourceSubresources]
    def __init__(
        self,
        *,
        additional_printer_columns: typing.Optional[list[kubernetes.client.V1CustomResourceColumnDefinition]] = ...,
        deprecated: typing.Optional[bool] = ...,
        deprecation_warning: typing.Optional[str] = ...,
        name: str,
        schema: typing.Optional[kubernetes.client.V1CustomResourceValidation] = ...,
        selectable_fields: typing.Optional[list[kubernetes.client.V1SelectableField]] = ...,
        served: bool,
        storage: bool,
        subresources: typing.Optional[kubernetes.client.V1CustomResourceSubresources] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
