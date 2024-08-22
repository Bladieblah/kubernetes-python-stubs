import typing

import kubernetes.client

class V1alpha2ResourceClass:
    api_version: typing.Optional[str]
    driver_name: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    parameters_ref: typing.Optional[kubernetes.client.V1alpha2ResourceClassParametersReference]
    structured_parameters: typing.Optional[bool]
    suitable_nodes: typing.Optional[kubernetes.client.V1NodeSelector]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        driver_name: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        parameters_ref: typing.Optional[kubernetes.client.V1alpha2ResourceClassParametersReference] = ...,
        structured_parameters: typing.Optional[bool] = ...,
        suitable_nodes: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
