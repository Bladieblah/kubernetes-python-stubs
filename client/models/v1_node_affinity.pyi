import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1NodeAffinity:
    preferred_during_scheduling_ignored_during_execution: typing.Optional[
        list[kubernetes.client.V1PreferredSchedulingTerm]
    ]
    required_during_scheduling_ignored_during_execution: typing.Optional[kubernetes.client.V1NodeSelector]
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[
            list[kubernetes.client.V1PreferredSchedulingTerm]
        ] = ...,
        required_during_scheduling_ignored_during_execution: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
