import typing

import kubernetes.client

class V1HTTPIngressPath:
    backend: kubernetes.client.V1IngressBackend
    path: typing.Optional[str]
    path_type: str
    def __init__(
        self, *, backend: kubernetes.client.V1IngressBackend, path: typing.Optional[str] = ..., path_type: str
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
