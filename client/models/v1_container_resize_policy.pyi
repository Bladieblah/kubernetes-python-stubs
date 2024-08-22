import typing

class V1ContainerResizePolicy:
    resource_name: str
    restart_policy: str
    def __init__(self, *, resource_name: str, restart_policy: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
