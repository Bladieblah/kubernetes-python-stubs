import typing

import kubernetes.client
from urllib3 import BaseHTTPResponse

class AuthorizationV1Api:
    def __init__(self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...) -> None: ...
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList: ...
    def create_namespaced_local_subject_access_review(
        self,
        namespace: str,
        body: kubernetes.client.V1LocalSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def create_self_subject_access_review(
        self,
        body: kubernetes.client.V1SelfSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def create_self_subject_rules_review(
        self,
        body: kubernetes.client.V1SelfSubjectRulesReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
    def create_subject_access_review(
        self,
        body: kubernetes.client.V1SubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
        _preload_content: bool = False,
    ) -> BaseHTTPResponse: ...
