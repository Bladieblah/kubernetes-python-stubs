import typing
from urllib3 import BaseHTTPResponse

class V1alpha2NamedResourcesStringSlice:
    strings: list[str]
    def __init__(self, *, strings: list[str]) -> None: ...
    def to_dict(self) -> typing.Any: ...
