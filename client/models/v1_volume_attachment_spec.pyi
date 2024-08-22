import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1VolumeAttachmentSpec:
    attacher: str
    node_name: str
    source: kubernetes.client.V1VolumeAttachmentSource
    def __init__(
        self, *, attacher: str, node_name: str, source: kubernetes.client.V1VolumeAttachmentSource
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
