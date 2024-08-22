import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1StatefulSetUpdateStrategy:
    rolling_update: typing.Optional[kubernetes.client.V1RollingUpdateStatefulSetStrategy]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        rolling_update: typing.Optional[kubernetes.client.V1RollingUpdateStatefulSetStrategy] = ...,
        type: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
