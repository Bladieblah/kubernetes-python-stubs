import typing

import kubernetes.client

class V1PodFailurePolicy:
    rules: list[kubernetes.client.V1PodFailurePolicyRule]
    def __init__(self, *, rules: list[kubernetes.client.V1PodFailurePolicyRule]) -> None: ...
    def to_dict(self) -> typing.Any: ...
