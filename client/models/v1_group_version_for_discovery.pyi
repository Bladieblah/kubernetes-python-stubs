import typing
from urllib3 import BaseHTTPResponse

class V1GroupVersionForDiscovery:
    group_version: str
    version: str
    def __init__(self, *, group_version: str, version: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
