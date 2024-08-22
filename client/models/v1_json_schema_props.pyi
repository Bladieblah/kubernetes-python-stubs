import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1JSONSchemaProps:
    ref: typing.Optional[str]
    schema: typing.Optional[str]
    additional_items: typing.Optional[typing.Any]
    additional_properties: typing.Optional[typing.Any]
    all_of: typing.Optional[list[kubernetes.client.V1JSONSchemaProps]]
    any_of: typing.Optional[list[kubernetes.client.V1JSONSchemaProps]]
    default: typing.Optional[typing.Any]
    definitions: typing.Optional[dict[str, kubernetes.client.V1JSONSchemaProps]]
    dependencies: typing.Optional[dict[str, typing.Any]]
    description: typing.Optional[str]
    enum: typing.Optional[list[typing.Any]]
    example: typing.Optional[typing.Any]
    exclusive_maximum: typing.Optional[bool]
    exclusive_minimum: typing.Optional[bool]
    external_docs: typing.Optional[kubernetes.client.V1ExternalDocumentation]
    format: typing.Optional[str]
    id: typing.Optional[str]
    items: typing.Optional[typing.Any]
    max_items: typing.Optional[int]
    max_length: typing.Optional[int]
    max_properties: typing.Optional[int]
    maximum: typing.Optional[float]
    min_items: typing.Optional[int]
    min_length: typing.Optional[int]
    min_properties: typing.Optional[int]
    minimum: typing.Optional[float]
    multiple_of: typing.Optional[float]
    _not: typing.Optional[kubernetes.client.V1JSONSchemaProps]
    nullable: typing.Optional[bool]
    one_of: typing.Optional[list[kubernetes.client.V1JSONSchemaProps]]
    pattern: typing.Optional[str]
    pattern_properties: typing.Optional[dict[str, kubernetes.client.V1JSONSchemaProps]]
    properties: typing.Optional[dict[str, kubernetes.client.V1JSONSchemaProps]]
    required: typing.Optional[list[str]]
    title: typing.Optional[str]
    type: typing.Optional[str]
    unique_items: typing.Optional[bool]
    x_kubernetes_embedded_resource: typing.Optional[bool]
    x_kubernetes_int_or_string: typing.Optional[bool]
    x_kubernetes_list_map_keys: typing.Optional[list[str]]
    x_kubernetes_list_type: typing.Optional[str]
    x_kubernetes_map_type: typing.Optional[str]
    x_kubernetes_preserve_unknown_fields: typing.Optional[bool]
    x_kubernetes_validations: typing.Optional[list[kubernetes.client.V1ValidationRule]]
    def __init__(
        self,
        *,
        ref: typing.Optional[str] = ...,
        schema: typing.Optional[str] = ...,
        additional_items: typing.Optional[typing.Any] = ...,
        additional_properties: typing.Optional[typing.Any] = ...,
        all_of: typing.Optional[list[kubernetes.client.V1JSONSchemaProps]] = ...,
        any_of: typing.Optional[list[kubernetes.client.V1JSONSchemaProps]] = ...,
        default: typing.Optional[typing.Any] = ...,
        definitions: typing.Optional[dict[str, kubernetes.client.V1JSONSchemaProps]] = ...,
        dependencies: typing.Optional[dict[str, typing.Any]] = ...,
        description: typing.Optional[str] = ...,
        enum: typing.Optional[list[typing.Any]] = ...,
        example: typing.Optional[typing.Any] = ...,
        exclusive_maximum: typing.Optional[bool] = ...,
        exclusive_minimum: typing.Optional[bool] = ...,
        external_docs: typing.Optional[kubernetes.client.V1ExternalDocumentation] = ...,
        format: typing.Optional[str] = ...,
        id: typing.Optional[str] = ...,
        items: typing.Optional[typing.Any] = ...,
        max_items: typing.Optional[int] = ...,
        max_length: typing.Optional[int] = ...,
        max_properties: typing.Optional[int] = ...,
        maximum: typing.Optional[float] = ...,
        min_items: typing.Optional[int] = ...,
        min_length: typing.Optional[int] = ...,
        min_properties: typing.Optional[int] = ...,
        minimum: typing.Optional[float] = ...,
        multiple_of: typing.Optional[float] = ...,
        _not: typing.Optional[kubernetes.client.V1JSONSchemaProps] = ...,
        nullable: typing.Optional[bool] = ...,
        one_of: typing.Optional[list[kubernetes.client.V1JSONSchemaProps]] = ...,
        pattern: typing.Optional[str] = ...,
        pattern_properties: typing.Optional[dict[str, kubernetes.client.V1JSONSchemaProps]] = ...,
        properties: typing.Optional[dict[str, kubernetes.client.V1JSONSchemaProps]] = ...,
        required: typing.Optional[list[str]] = ...,
        title: typing.Optional[str] = ...,
        type: typing.Optional[str] = ...,
        unique_items: typing.Optional[bool] = ...,
        x_kubernetes_embedded_resource: typing.Optional[bool] = ...,
        x_kubernetes_int_or_string: typing.Optional[bool] = ...,
        x_kubernetes_list_map_keys: typing.Optional[list[str]] = ...,
        x_kubernetes_list_type: typing.Optional[str] = ...,
        x_kubernetes_map_type: typing.Optional[str] = ...,
        x_kubernetes_preserve_unknown_fields: typing.Optional[bool] = ...,
        x_kubernetes_validations: typing.Optional[list[kubernetes.client.V1ValidationRule]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
