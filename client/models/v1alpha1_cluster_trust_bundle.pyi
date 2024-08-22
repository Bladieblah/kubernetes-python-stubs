import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha1ClusterTrustBundle:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1alpha1ClusterTrustBundleSpec
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha1ClusterTrustBundleSpec,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
