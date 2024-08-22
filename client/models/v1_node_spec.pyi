import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1NodeSpec:
    config_source: typing.Optional[kubernetes.client.V1NodeConfigSource]
    external_id: typing.Optional[str]
    pod_cidr: typing.Optional[str]
    pod_cid_rs: typing.Optional[list[str]]
    provider_id: typing.Optional[str]
    taints: typing.Optional[list[kubernetes.client.V1Taint]]
    unschedulable: typing.Optional[bool]
    def __init__(
        self,
        *,
        config_source: typing.Optional[kubernetes.client.V1NodeConfigSource] = ...,
        external_id: typing.Optional[str] = ...,
        pod_cidr: typing.Optional[str] = ...,
        pod_cid_rs: typing.Optional[list[str]] = ...,
        provider_id: typing.Optional[str] = ...,
        taints: typing.Optional[list[kubernetes.client.V1Taint]] = ...,
        unschedulable: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
