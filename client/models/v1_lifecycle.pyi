import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1Lifecycle:
    post_start: typing.Optional[kubernetes.client.V1LifecycleHandler]
    pre_stop: typing.Optional[kubernetes.client.V1LifecycleHandler]
    def __init__(
        self,
        *,
        post_start: typing.Optional[kubernetes.client.V1LifecycleHandler] = ...,
        pre_stop: typing.Optional[kubernetes.client.V1LifecycleHandler] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
