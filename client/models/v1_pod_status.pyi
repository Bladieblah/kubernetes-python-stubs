import datetime
import typing

import kubernetes.client

class V1PodStatus:
    conditions: typing.Optional[list[kubernetes.client.V1PodCondition]]
    container_statuses: typing.Optional[list[kubernetes.client.V1ContainerStatus]]
    ephemeral_container_statuses: typing.Optional[list[kubernetes.client.V1ContainerStatus]]
    host_ip: typing.Optional[str]
    host_i_ps: typing.Optional[list[kubernetes.client.V1HostIP]]
    init_container_statuses: typing.Optional[list[kubernetes.client.V1ContainerStatus]]
    message: typing.Optional[str]
    nominated_node_name: typing.Optional[str]
    phase: typing.Optional[str]
    pod_ip: typing.Optional[str]
    pod_i_ps: typing.Optional[list[kubernetes.client.V1PodIP]]
    qos_class: typing.Optional[str]
    reason: typing.Optional[str]
    resize: typing.Optional[str]
    resource_claim_statuses: typing.Optional[list[kubernetes.client.V1PodResourceClaimStatus]]
    start_time: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes.client.V1PodCondition]] = ...,
        container_statuses: typing.Optional[list[kubernetes.client.V1ContainerStatus]] = ...,
        ephemeral_container_statuses: typing.Optional[list[kubernetes.client.V1ContainerStatus]] = ...,
        host_ip: typing.Optional[str] = ...,
        host_i_ps: typing.Optional[list[kubernetes.client.V1HostIP]] = ...,
        init_container_statuses: typing.Optional[list[kubernetes.client.V1ContainerStatus]] = ...,
        message: typing.Optional[str] = ...,
        nominated_node_name: typing.Optional[str] = ...,
        phase: typing.Optional[str] = ...,
        pod_ip: typing.Optional[str] = ...,
        pod_i_ps: typing.Optional[list[kubernetes.client.V1PodIP]] = ...,
        qos_class: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        resize: typing.Optional[str] = ...,
        resource_claim_statuses: typing.Optional[list[kubernetes.client.V1PodResourceClaimStatus]] = ...,
        start_time: typing.Optional[datetime.datetime] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
