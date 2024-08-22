import typing

import kubernetes.client

class V1alpha2PodSchedulingContextStatus:
    resource_claims: typing.Optional[list[kubernetes.client.V1alpha2ResourceClaimSchedulingStatus]]
    def __init__(
        self, *, resource_claims: typing.Optional[list[kubernetes.client.V1alpha2ResourceClaimSchedulingStatus]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
