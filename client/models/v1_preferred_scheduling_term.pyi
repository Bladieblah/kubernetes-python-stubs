import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1PreferredSchedulingTerm:
    preference: kubernetes.client.V1NodeSelectorTerm
    weight: int
    def __init__(self, *, preference: kubernetes.client.V1NodeSelectorTerm, weight: int) -> None: ...
    def to_dict(self) -> typing.Any: ...
