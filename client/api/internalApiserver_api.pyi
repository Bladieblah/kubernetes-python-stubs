import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class InternalApiserverApi:
    def __init__(self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...) -> None: ...
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
