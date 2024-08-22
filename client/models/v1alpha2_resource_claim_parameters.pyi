import typing

import kubernetes.client

class V1alpha2ResourceClaimParameters:
    api_version: typing.Optional[str]
    driver_requests: typing.Optional[list[kubernetes.client.V1alpha2DriverRequests]]
    generated_from: typing.Optional[kubernetes.client.V1alpha2ResourceClaimParametersReference]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    shareable: typing.Optional[bool]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        driver_requests: typing.Optional[list[kubernetes.client.V1alpha2DriverRequests]] = ...,
        generated_from: typing.Optional[kubernetes.client.V1alpha2ResourceClaimParametersReference] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        shareable: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
