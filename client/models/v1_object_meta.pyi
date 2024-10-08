import datetime
import typing

import kubernetes.client

class V1ObjectMeta:
    annotations: typing.Optional[dict[str, str]]
    creation_timestamp: typing.Optional[datetime.datetime]
    deletion_grace_period_seconds: typing.Optional[int]
    deletion_timestamp: typing.Optional[datetime.datetime]
    finalizers: typing.Optional[list[str]]
    generate_name: typing.Optional[str]
    generation: typing.Optional[int]
    labels: typing.Optional[dict[str, str]]
    managed_fields: typing.Optional[list[kubernetes.client.V1ManagedFieldsEntry]]
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    owner_references: typing.Optional[list[kubernetes.client.V1OwnerReference]]
    resource_version: typing.Optional[str]
    self_link: typing.Optional[str]
    uid: typing.Optional[str]
    def __init__(
        self,
        *,
        annotations: typing.Optional[dict[str, str]] = ...,
        creation_timestamp: typing.Optional[datetime.datetime] = ...,
        deletion_grace_period_seconds: typing.Optional[int] = ...,
        deletion_timestamp: typing.Optional[datetime.datetime] = ...,
        finalizers: typing.Optional[list[str]] = ...,
        generate_name: typing.Optional[str] = ...,
        generation: typing.Optional[int] = ...,
        labels: typing.Optional[dict[str, str]] = ...,
        managed_fields: typing.Optional[list[kubernetes.client.V1ManagedFieldsEntry]] = ...,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        owner_references: typing.Optional[list[kubernetes.client.V1OwnerReference]] = ...,
        resource_version: typing.Optional[str] = ...,
        self_link: typing.Optional[str] = ...,
        uid: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
