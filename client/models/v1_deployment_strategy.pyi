import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1DeploymentStrategy:
    rolling_update: typing.Optional[kubernetes.client.V1RollingUpdateDeployment]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        rolling_update: typing.Optional[kubernetes.client.V1RollingUpdateDeployment] = ...,
        type: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
