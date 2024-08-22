import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1VolumeAttachmentSource:
    inline_volume_spec: typing.Optional[kubernetes.client.V1PersistentVolumeSpec]
    persistent_volume_name: typing.Optional[str]
    def __init__(
        self,
        *,
        inline_volume_spec: typing.Optional[kubernetes.client.V1PersistentVolumeSpec] = ...,
        persistent_volume_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
