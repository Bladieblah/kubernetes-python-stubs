import typing
from urllib3 import BaseHTTPResponse

class V1CustomResourceSubresourceScale:
    label_selector_path: typing.Optional[str]
    spec_replicas_path: str
    status_replicas_path: str
    def __init__(
        self, *, label_selector_path: typing.Optional[str] = ..., spec_replicas_path: str, status_replicas_path: str
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
