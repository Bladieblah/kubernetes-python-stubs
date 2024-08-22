import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1alpha1ParamRef:
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    parameter_not_found_action: typing.Optional[str]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    def __init__(
        self,
        *,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        parameter_not_found_action: typing.Optional[str] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
