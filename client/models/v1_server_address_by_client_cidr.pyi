import typing

class V1ServerAddressByClientCIDR:
    client_cidr: str
    server_address: str
    def __init__(self, *, client_cidr: str, server_address: str) -> None: ...
    def to_dict(self) -> typing.Any: ...
