import typing

class V1WindowsSecurityContextOptions:
    gmsa_credential_spec: typing.Optional[str]
    gmsa_credential_spec_name: typing.Optional[str]
    host_process: typing.Optional[bool]
    run_as_user_name: typing.Optional[str]
    def __init__(
        self,
        *,
        gmsa_credential_spec: typing.Optional[str] = ...,
        gmsa_credential_spec_name: typing.Optional[str] = ...,
        host_process: typing.Optional[bool] = ...,
        run_as_user_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
