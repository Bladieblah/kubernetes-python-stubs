import typing

class V1VsphereVirtualDiskVolumeSource:
    fs_type: typing.Optional[str]
    storage_policy_id: typing.Optional[str]
    storage_policy_name: typing.Optional[str]
    volume_path: str
    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        storage_policy_id: typing.Optional[str] = ...,
        storage_policy_name: typing.Optional[str] = ...,
        volume_path: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
