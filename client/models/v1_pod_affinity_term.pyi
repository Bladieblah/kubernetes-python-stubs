import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1PodAffinityTerm:
    label_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    match_label_keys: typing.Optional[list[str]]
    mismatch_label_keys: typing.Optional[list[str]]
    namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    namespaces: typing.Optional[list[str]]
    topology_key: str
    def __init__(
        self,
        *,
        label_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        match_label_keys: typing.Optional[list[str]] = ...,
        mismatch_label_keys: typing.Optional[list[str]] = ...,
        namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        namespaces: typing.Optional[list[str]] = ...,
        topology_key: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
