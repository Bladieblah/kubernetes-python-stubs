import typing

import kubernetes.client

class V1ISCSIPersistentVolumeSource:
    chap_auth_discovery: typing.Optional[bool]
    chap_auth_session: typing.Optional[bool]
    fs_type: typing.Optional[str]
    initiator_name: typing.Optional[str]
    iqn: str
    iscsi_interface: typing.Optional[str]
    lun: int
    portals: typing.Optional[list[str]]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes.client.V1SecretReference]
    target_portal: str
    def __init__(
        self,
        *,
        chap_auth_discovery: typing.Optional[bool] = ...,
        chap_auth_session: typing.Optional[bool] = ...,
        fs_type: typing.Optional[str] = ...,
        initiator_name: typing.Optional[str] = ...,
        iqn: str,
        iscsi_interface: typing.Optional[str] = ...,
        lun: int,
        portals: typing.Optional[list[str]] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[kubernetes.client.V1SecretReference] = ...,
        target_portal: str,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
