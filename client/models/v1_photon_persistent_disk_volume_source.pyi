import typing

class V1PhotonPersistentDiskVolumeSource:
    fs_type: typing.Optional[str]
    pd_id: str
    def __init__(self, *, fs_type: typing.Optional[str] = ..., pd_id: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
