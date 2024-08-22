import typing

class V1alpha1ClusterTrustBundleSpec:
    signer_name: typing.Optional[str]
    trust_bundle: str
    def __init__(self, *, signer_name: typing.Optional[str] = ..., trust_bundle: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
