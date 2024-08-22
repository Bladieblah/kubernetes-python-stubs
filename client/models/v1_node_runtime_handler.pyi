import typing

import kubernetes.client

class V1NodeRuntimeHandler:
    features: typing.Optional[kubernetes.client.V1NodeRuntimeHandlerFeatures]
    name: typing.Optional[str]
    def __init__(
        self,
        *,
        features: typing.Optional[kubernetes.client.V1NodeRuntimeHandlerFeatures] = ...,
        name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
