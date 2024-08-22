import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1beta3PriorityLevelConfigurationSpec:
    exempt: typing.Optional[kubernetes.client.V1beta3ExemptPriorityLevelConfiguration]
    limited: typing.Optional[kubernetes.client.V1beta3LimitedPriorityLevelConfiguration]
    type: str
    def __init__(
        self,
        *,
        exempt: typing.Optional[kubernetes.client.V1beta3ExemptPriorityLevelConfiguration] = ...,
        limited: typing.Optional[kubernetes.client.V1beta3LimitedPriorityLevelConfiguration] = ...,
        type: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
