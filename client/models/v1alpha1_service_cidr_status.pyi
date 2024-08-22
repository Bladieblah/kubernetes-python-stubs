import typing

import kubernetes.client

class V1alpha1ServiceCIDRStatus:
    conditions: typing.Optional[list[kubernetes.client.V1Condition]]
    def __init__(self, *, conditions: typing.Optional[list[kubernetes.client.V1Condition]] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
