import typing

import kubernetes.client

class V1beta3LimitResponse:
    queuing: typing.Optional[kubernetes.client.V1beta3QueuingConfiguration]
    type: str
    def __init__(
        self, *, queuing: typing.Optional[kubernetes.client.V1beta3QueuingConfiguration] = ..., type: str
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
