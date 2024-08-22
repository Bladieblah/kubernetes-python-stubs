import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CephFSVolumeSource:
    monitors: list[str]
    path: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_file: typing.Optional[str]
    secret_ref: typing.Optional[kubernetes.client.V1LocalObjectReference]
    user: typing.Optional[str]
    def __init__(
        self,
        *,
        monitors: list[str],
        path: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_file: typing.Optional[str] = ...,
        secret_ref: typing.Optional[kubernetes.client.V1LocalObjectReference] = ...,
        user: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
