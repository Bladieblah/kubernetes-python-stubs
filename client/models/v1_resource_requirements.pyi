import typing

import kubernetes.client

class V1ResourceRequirements:
    claims: typing.Optional[list[kubernetes.client.V1ResourceClaim]]
    limits: typing.Optional[dict[str, str]]
    requests: typing.Optional[dict[str, str]]
    def __init__(
        self,
        *,
        claims: typing.Optional[list[kubernetes.client.V1ResourceClaim]] = ...,
        limits: typing.Optional[dict[str, str]] = ...,
        requests: typing.Optional[dict[str, str]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
