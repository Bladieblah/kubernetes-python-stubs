import typing
from urllib3 import BaseHTTPResponse

class V1alpha2NamedResourcesIntSlice:
    ints: list[int]
    def __init__(self, *, ints: list[int]) -> None: ...
    def to_dict(self) -> typing.Any: ...
