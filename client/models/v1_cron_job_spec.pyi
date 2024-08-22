import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1CronJobSpec:
    concurrency_policy: typing.Optional[str]
    failed_jobs_history_limit: typing.Optional[int]
    job_template: kubernetes.client.V1JobTemplateSpec
    schedule: str
    starting_deadline_seconds: typing.Optional[int]
    successful_jobs_history_limit: typing.Optional[int]
    suspend: typing.Optional[bool]
    time_zone: typing.Optional[str]
    def __init__(
        self,
        *,
        concurrency_policy: typing.Optional[str] = ...,
        failed_jobs_history_limit: typing.Optional[int] = ...,
        job_template: kubernetes.client.V1JobTemplateSpec,
        schedule: str,
        starting_deadline_seconds: typing.Optional[int] = ...,
        successful_jobs_history_limit: typing.Optional[int] = ...,
        suspend: typing.Optional[bool] = ...,
        time_zone: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
