import typing
from urllib3 import BaseHTTPResponse

class V1FlowDistinguisherMethod:
    type: str
    def __init__(self, *, type: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
