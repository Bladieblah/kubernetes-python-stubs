import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1PersistentVolumeClaimSpec:
    access_modes: typing.Optional[list[str]]
    data_source: typing.Optional[kubernetes.client.V1TypedLocalObjectReference]
    data_source_ref: typing.Optional[kubernetes.client.V1TypedObjectReference]
    resources: typing.Optional[kubernetes.client.V1VolumeResourceRequirements]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    storage_class_name: typing.Optional[str]
    volume_attributes_class_name: typing.Optional[str]
    volume_mode: typing.Optional[str]
    volume_name: typing.Optional[str]
    def __init__(
        self,
        *,
        access_modes: typing.Optional[list[str]] = ...,
        data_source: typing.Optional[kubernetes.client.V1TypedLocalObjectReference] = ...,
        data_source_ref: typing.Optional[kubernetes.client.V1TypedObjectReference] = ...,
        resources: typing.Optional[kubernetes.client.V1VolumeResourceRequirements] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        storage_class_name: typing.Optional[str] = ...,
        volume_attributes_class_name: typing.Optional[str] = ...,
        volume_mode: typing.Optional[str] = ...,
        volume_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
