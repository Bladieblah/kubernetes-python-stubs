import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1PodFailurePolicyRule:
    action: str
    on_exit_codes: typing.Optional[kubernetes.client.V1PodFailurePolicyOnExitCodesRequirement]
    on_pod_conditions: typing.Optional[list[kubernetes.client.V1PodFailurePolicyOnPodConditionsPattern]]
    def __init__(
        self,
        *,
        action: str,
        on_exit_codes: typing.Optional[kubernetes.client.V1PodFailurePolicyOnExitCodesRequirement] = ...,
        on_pod_conditions: typing.Optional[list[kubernetes.client.V1PodFailurePolicyOnPodConditionsPattern]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
