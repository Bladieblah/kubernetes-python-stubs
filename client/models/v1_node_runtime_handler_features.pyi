import typing
from urllib3 import BaseHTTPResponse

class V1NodeRuntimeHandlerFeatures:
    recursive_read_only_mounts: typing.Optional[bool]
    def __init__(self, *, recursive_read_only_mounts: typing.Optional[bool] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
