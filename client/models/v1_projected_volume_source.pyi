import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1ProjectedVolumeSource:
    default_mode: typing.Optional[int]
    sources: typing.Optional[list[kubernetes.client.V1VolumeProjection]]
    def __init__(
        self,
        *,
        default_mode: typing.Optional[int] = ...,
        sources: typing.Optional[list[kubernetes.client.V1VolumeProjection]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
