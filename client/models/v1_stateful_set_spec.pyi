import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1StatefulSetSpec:
    min_ready_seconds: typing.Optional[int]
    ordinals: typing.Optional[kubernetes.client.V1StatefulSetOrdinals]
    persistent_volume_claim_retention_policy: typing.Optional[
        kubernetes.client.V1StatefulSetPersistentVolumeClaimRetentionPolicy
    ]
    pod_management_policy: typing.Optional[str]
    replicas: typing.Optional[int]
    revision_history_limit: typing.Optional[int]
    selector: kubernetes.client.V1LabelSelector
    service_name: str
    template: kubernetes.client.V1PodTemplateSpec
    update_strategy: typing.Optional[kubernetes.client.V1StatefulSetUpdateStrategy]
    volume_claim_templates: typing.Optional[list[kubernetes.client.V1PersistentVolumeClaim]]
    def __init__(
        self,
        *,
        min_ready_seconds: typing.Optional[int] = ...,
        ordinals: typing.Optional[kubernetes.client.V1StatefulSetOrdinals] = ...,
        persistent_volume_claim_retention_policy: typing.Optional[
            kubernetes.client.V1StatefulSetPersistentVolumeClaimRetentionPolicy
        ] = ...,
        pod_management_policy: typing.Optional[str] = ...,
        replicas: typing.Optional[int] = ...,
        revision_history_limit: typing.Optional[int] = ...,
        selector: kubernetes.client.V1LabelSelector,
        service_name: str,
        template: kubernetes.client.V1PodTemplateSpec,
        update_strategy: typing.Optional[kubernetes.client.V1StatefulSetUpdateStrategy] = ...,
        volume_claim_templates: typing.Optional[list[kubernetes.client.V1PersistentVolumeClaim]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
