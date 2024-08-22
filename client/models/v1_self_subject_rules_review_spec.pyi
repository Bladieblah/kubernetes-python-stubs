import typing
from urllib3 import BaseHTTPResponse

class V1SelfSubjectRulesReviewSpec:
    namespace: typing.Optional[str]
    def __init__(self, *, namespace: typing.Optional[str] = ...) -> None: ...
    def to_dict(self) -> typing.Any: ...
