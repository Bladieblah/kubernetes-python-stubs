import typing

import kubernetes.client

class VersionApi:
    def __init__(self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...) -> None: ...
    def get_code(self) -> kubernetes.client.VersionInfo: ...
