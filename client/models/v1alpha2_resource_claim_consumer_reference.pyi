import typing
from urllib3 import BaseHTTPResponse

class V1alpha2ResourceClaimConsumerReference:
    api_group: typing.Optional[str]
    name: str
    resource: str
    uid: str
    def __init__(self, *, api_group: typing.Optional[str] = ..., name: str, resource: str, uid: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
