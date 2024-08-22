import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha1VolumeAttributesClass:
    api_version: typing.Optional[str]
    driver_name: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    parameters: typing.Optional[dict[str, str]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        driver_name: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        parameters: typing.Optional[dict[str, str]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
