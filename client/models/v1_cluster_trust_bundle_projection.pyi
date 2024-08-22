import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ClusterTrustBundleProjection:
    label_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    name: typing.Optional[str]
    optional: typing.Optional[bool]
    path: str
    signer_name: typing.Optional[str]
    def __init__(
        self,
        *,
        label_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        name: typing.Optional[str] = ...,
        optional: typing.Optional[bool] = ...,
        path: str,
        signer_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
