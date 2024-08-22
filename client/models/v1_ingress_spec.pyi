import typing

import kubernetes.client

class V1IngressSpec:
    default_backend: typing.Optional[kubernetes.client.V1IngressBackend]
    ingress_class_name: typing.Optional[str]
    rules: typing.Optional[list[kubernetes.client.V1IngressRule]]
    tls: typing.Optional[list[kubernetes.client.V1IngressTLS]]
    def __init__(
        self,
        *,
        default_backend: typing.Optional[kubernetes.client.V1IngressBackend] = ...,
        ingress_class_name: typing.Optional[str] = ...,
        rules: typing.Optional[list[kubernetes.client.V1IngressRule]] = ...,
        tls: typing.Optional[list[kubernetes.client.V1IngressTLS]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
