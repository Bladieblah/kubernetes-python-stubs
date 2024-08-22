import typing

class V1NetworkPolicyPort:
    end_port: typing.Optional[int]
    port: typing.Optional[typing.Any]
    protocol: typing.Optional[str]
    def __init__(
        self,
        *,
        end_port: typing.Optional[int] = ...,
        port: typing.Optional[typing.Any] = ...,
        protocol: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
