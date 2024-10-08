import typing

class V1ClaimSource:
    resource_claim_name: typing.Optional[str]
    resource_claim_template_name: typing.Optional[str]
    def __init__(
        self,
        *,
        resource_claim_name: typing.Optional[str] = ...,
        resource_claim_template_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
