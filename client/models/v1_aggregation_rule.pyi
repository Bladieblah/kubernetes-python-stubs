import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1AggregationRule:
    cluster_role_selectors: typing.Optional[list[kubernetes.client.V1LabelSelector]]
    def __init__(
        self, *, cluster_role_selectors: typing.Optional[list[kubernetes.client.V1LabelSelector]] = ...
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
