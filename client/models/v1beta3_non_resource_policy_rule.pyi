import typing

class V1beta3NonResourcePolicyRule:
    non_resource_ur_ls: list[str]
    verbs: list[str]
    def __init__(self, *, non_resource_ur_ls: list[str], verbs: list[str]) -> None: ...
    def to_dict(self) -> typing.Any: ...
