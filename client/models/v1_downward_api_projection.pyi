import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1DownwardAPIProjection:
    items: typing.Optional[list[kubernetes.client.V1DownwardAPIVolumeFile]]
    def __init__(self, *, items: typing.Optional[list[kubernetes.client.V1DownwardAPIVolumeFile]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
