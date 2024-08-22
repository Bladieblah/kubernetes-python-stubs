import typing
from urllib3 import BaseHTTPResponse

class V1StatefulSetPersistentVolumeClaimRetentionPolicy:
    when_deleted: typing.Optional[str]
    when_scaled: typing.Optional[str]
    def __init__(
        self, *, when_deleted: typing.Optional[str] = ..., when_scaled: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
