import typing

class V1ConfigMapNodeConfigSource:
    kubelet_config_key: str
    name: str
    namespace: str
    resource_version: typing.Optional[str]
    uid: typing.Optional[str]
    def __init__(
        self,
        *,
        kubelet_config_key: str,
        name: str,
        namespace: str,
        resource_version: typing.Optional[str] = ...,
        uid: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
