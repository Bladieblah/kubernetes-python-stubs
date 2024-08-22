import typing

import kubernetes.client

class V1APIVersions:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    server_address_by_client_cid_rs: list[kubernetes.client.V1ServerAddressByClientCIDR]
    versions: list[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        server_address_by_client_cid_rs: list[kubernetes.client.V1ServerAddressByClientCIDR],
        versions: list[str],
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
