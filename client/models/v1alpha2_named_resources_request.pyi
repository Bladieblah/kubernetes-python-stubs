import typing
from urllib3 import BaseHTTPResponse

class V1alpha2NamedResourcesRequest:
    selector: str
    def __init__(self, *, selector: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
