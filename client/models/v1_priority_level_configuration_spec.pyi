import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1PriorityLevelConfigurationSpec:
    exempt: typing.Optional[kubernetes.client.V1ExemptPriorityLevelConfiguration]
    limited: typing.Optional[kubernetes.client.V1LimitedPriorityLevelConfiguration]
    type: str
    def __init__(
        self,
        *,
        exempt: typing.Optional[kubernetes.client.V1ExemptPriorityLevelConfiguration] = ...,
        limited: typing.Optional[kubernetes.client.V1LimitedPriorityLevelConfiguration] = ...,
        type: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
