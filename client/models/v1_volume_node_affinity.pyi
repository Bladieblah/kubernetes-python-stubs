import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1VolumeNodeAffinity:
    required: typing.Optional[kubernetes.client.V1NodeSelector]
    def __init__(self, *, required: typing.Optional[kubernetes.client.V1NodeSelector] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
