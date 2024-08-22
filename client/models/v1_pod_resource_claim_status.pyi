import typing
from urllib3 import BaseHTTPResponse

class V1PodResourceClaimStatus:
    name: str
    resource_claim_name: typing.Optional[str]
    def __init__(self, *, name: str, resource_claim_name: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
