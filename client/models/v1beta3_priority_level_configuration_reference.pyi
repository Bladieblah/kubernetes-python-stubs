import typing
from urllib3 import BaseHTTPResponse

class V1beta3PriorityLevelConfigurationReference:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
