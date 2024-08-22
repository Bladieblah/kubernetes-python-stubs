import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V2MetricSpec:
    container_resource: typing.Optional[kubernetes.client.V2ContainerResourceMetricSource]
    external: typing.Optional[kubernetes.client.V2ExternalMetricSource]
    object: typing.Optional[kubernetes.client.V2ObjectMetricSource]
    pods: typing.Optional[kubernetes.client.V2PodsMetricSource]
    resource: typing.Optional[kubernetes.client.V2ResourceMetricSource]
    type: str
    def __init__(
        self,
        *,
        container_resource: typing.Optional[kubernetes.client.V2ContainerResourceMetricSource] = ...,
        external: typing.Optional[kubernetes.client.V2ExternalMetricSource] = ...,
        object: typing.Optional[kubernetes.client.V2ObjectMetricSource] = ...,
        pods: typing.Optional[kubernetes.client.V2PodsMetricSource] = ...,
        resource: typing.Optional[kubernetes.client.V2ResourceMetricSource] = ...,
        type: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
