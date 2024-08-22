import typing

import kubernetes.client

class V1CSIDriverSpec:
    attach_required: typing.Optional[bool]
    fs_group_policy: typing.Optional[str]
    pod_info_on_mount: typing.Optional[bool]
    requires_republish: typing.Optional[bool]
    se_linux_mount: typing.Optional[bool]
    storage_capacity: typing.Optional[bool]
    token_requests: typing.Optional[list[kubernetes.client.StorageV1TokenRequest]]
    volume_lifecycle_modes: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        attach_required: typing.Optional[bool] = ...,
        fs_group_policy: typing.Optional[str] = ...,
        pod_info_on_mount: typing.Optional[bool] = ...,
        requires_republish: typing.Optional[bool] = ...,
        se_linux_mount: typing.Optional[bool] = ...,
        storage_capacity: typing.Optional[bool] = ...,
        token_requests: typing.Optional[list[kubernetes.client.StorageV1TokenRequest]] = ...,
        volume_lifecycle_modes: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
