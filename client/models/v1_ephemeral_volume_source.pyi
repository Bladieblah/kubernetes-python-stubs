import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1EphemeralVolumeSource:
    volume_claim_template: typing.Optional[kubernetes.client.V1PersistentVolumeClaimTemplate]
    def __init__(
        self, *, volume_claim_template: typing.Optional[kubernetes.client.V1PersistentVolumeClaimTemplate] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
