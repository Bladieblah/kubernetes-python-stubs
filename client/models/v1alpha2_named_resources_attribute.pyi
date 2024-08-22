import typing

import kubernetes.client

class V1alpha2NamedResourcesAttribute:
    bool: typing.Optional[bool]
    int: typing.Optional[int]
    int_slice: typing.Optional[kubernetes.client.V1alpha2NamedResourcesIntSlice]
    name: str
    quantity: typing.Optional[str]
    string: typing.Optional[str]
    string_slice: typing.Optional[kubernetes.client.V1alpha2NamedResourcesStringSlice]
    version: typing.Optional[str]
    def __init__(
        self,
        *,
        bool: typing.Optional[bool] = ...,
        int: typing.Optional[int] = ...,
        int_slice: typing.Optional[kubernetes.client.V1alpha2NamedResourcesIntSlice] = ...,
        name: str,
        quantity: typing.Optional[str] = ...,
        string: typing.Optional[str] = ...,
        string_slice: typing.Optional[kubernetes.client.V1alpha2NamedResourcesStringSlice] = ...,
        version: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
