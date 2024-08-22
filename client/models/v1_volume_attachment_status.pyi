import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1VolumeAttachmentStatus:
    attach_error: typing.Optional[kubernetes.client.V1VolumeError]
    attached: bool
    attachment_metadata: typing.Optional[dict[str, str]]
    detach_error: typing.Optional[kubernetes.client.V1VolumeError]
    def __init__(
        self,
        *,
        attach_error: typing.Optional[kubernetes.client.V1VolumeError] = ...,
        attached: bool,
        attachment_metadata: typing.Optional[dict[str, str]] = ...,
        detach_error: typing.Optional[kubernetes.client.V1VolumeError] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
