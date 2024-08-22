import typing

class V1alpha1ServerStorageVersion:
    api_server_id: typing.Optional[str]
    decodable_versions: typing.Optional[list[str]]
    encoding_version: typing.Optional[str]
    served_versions: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        api_server_id: typing.Optional[str] = ...,
        decodable_versions: typing.Optional[list[str]] = ...,
        encoding_version: typing.Optional[str] = ...,
        served_versions: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
