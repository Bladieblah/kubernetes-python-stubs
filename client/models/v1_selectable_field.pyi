import typing
from urllib3 import BaseHTTPResponse

class V1SelectableField:
    json_path: str
    def __init__(self, *, json_path: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
