import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1NodeConfigSource:
    config_map: typing.Optional[kubernetes.client.V1ConfigMapNodeConfigSource]
    def __init__(self, *, config_map: typing.Optional[kubernetes.client.V1ConfigMapNodeConfigSource] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
