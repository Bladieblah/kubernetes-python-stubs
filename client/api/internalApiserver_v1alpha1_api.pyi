import typing

import kubernetes.client
from urllib3 import BaseHTTPResponse

class InternalApiserverV1alpha1Api:
    def __init__(self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...) -> None: ...
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList: ...
    def list_storage_version(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def create_storage_version(
        self,
        body: kubernetes.client.V1alpha1StorageVersion,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def delete_collection_storage_version(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        _continue: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def read_storage_version(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def replace_storage_version(
        self,
        name: str,
        body: kubernetes.client.V1alpha1StorageVersion,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def delete_storage_version(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def patch_storage_version(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def read_storage_version_status(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def replace_storage_version_status(
        self,
        name: str,
        body: kubernetes.client.V1alpha1StorageVersion,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def patch_storage_version_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
