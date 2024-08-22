from multiprocessing.pool import ThreadPool
from typing import Any, Dict, List, Optional, Protocol, Type, TypeVar

from kubernetes.client import Configuration
from kubernetes.client.rest import RESTClientObject

_T = TypeVar("_T")

class Response(Protocol):
    data: str

class ApiClient:
    user_agent: str
    pool: ThreadPool
    configuration: Configuration
    pool_threads: int
    rest_client: RESTClientObject
    default_headers: Dict[str, str]
    cookie: Any
    user_agent: str
    client_side_validation: bool

    def __init__(self, configuration: Optional[Configuration] = None) -> None: ...
    def sanitize_for_serialization(self, obj: Any) -> dict[Any, Any]: ...
    def deserialize(self, response: Response, response_type: Type[_T]) -> _T: ...
    def select_header_accept(self, accepts: List[str]) -> str: ...
    def select_header_content_type(self, content_types: List[str]) -> str: ...
    def call_api(
        self,
        resource_path: str,
        method: str,
        path_params,
        query_params,
        header_params,
        body=None,
        post_params=None,
        files=None,
        response_type=None,
        auth_settings=None,
        async_req=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
        _host=None,
    ): ...
