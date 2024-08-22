import typing
from urllib3 import BaseHTTPResponse

class V1alpha2VendorParameters:
    driver_name: typing.Optional[str]
    parameters: typing.Optional[typing.Any]
    def __init__(
        self, *, driver_name: typing.Optional[str] = ..., parameters: typing.Optional[typing.Any] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
