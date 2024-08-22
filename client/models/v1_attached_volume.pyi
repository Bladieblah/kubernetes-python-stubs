import typing
from urllib3 import BaseHTTPResponse

class V1AttachedVolume:
    device_path: str
    name: str
    def __init__(self, *, device_path: str, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
