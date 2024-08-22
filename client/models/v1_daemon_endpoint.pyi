import typing
from urllib3 import BaseHTTPResponse

class V1DaemonEndpoint:
    port: int
    def __init__(self, *, port: int) -> None: ...
    def to_dict(self) -> typing.Any: ...
