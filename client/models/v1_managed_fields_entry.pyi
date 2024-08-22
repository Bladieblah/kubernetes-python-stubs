import datetime
import typing
from urllib3 import BaseHTTPResponse

class V1ManagedFieldsEntry:
    api_version: typing.Optional[str]
    fields_type: typing.Optional[str]
    fields_v1: typing.Optional[typing.Any]
    manager: typing.Optional[str]
    operation: typing.Optional[str]
    subresource: typing.Optional[str]
    time: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        fields_type: typing.Optional[str] = ...,
        fields_v1: typing.Optional[typing.Any] = ...,
        manager: typing.Optional[str] = ...,
        operation: typing.Optional[str] = ...,
        subresource: typing.Optional[str] = ...,
        time: typing.Optional[datetime.datetime] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
