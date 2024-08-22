import datetime
import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class EventsV1Event:
    action: typing.Optional[str]
    api_version: typing.Optional[str]
    deprecated_count: typing.Optional[int]
    deprecated_first_timestamp: typing.Optional[datetime.datetime]
    deprecated_last_timestamp: typing.Optional[datetime.datetime]
    deprecated_source: typing.Optional[kubernetes.client.V1EventSource]
    event_time: datetime.datetime
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    note: typing.Optional[str]
    reason: typing.Optional[str]
    regarding: typing.Optional[kubernetes.client.V1ObjectReference]
    related: typing.Optional[kubernetes.client.V1ObjectReference]
    reporting_controller: typing.Optional[str]
    reporting_instance: typing.Optional[str]
    series: typing.Optional[kubernetes.client.EventsV1EventSeries]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        action: typing.Optional[str] = ...,
        api_version: typing.Optional[str] = ...,
        deprecated_count: typing.Optional[int] = ...,
        deprecated_first_timestamp: typing.Optional[datetime.datetime] = ...,
        deprecated_last_timestamp: typing.Optional[datetime.datetime] = ...,
        deprecated_source: typing.Optional[kubernetes.client.V1EventSource] = ...,
        event_time: datetime.datetime,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        note: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        regarding: typing.Optional[kubernetes.client.V1ObjectReference] = ...,
        related: typing.Optional[kubernetes.client.V1ObjectReference] = ...,
        reporting_controller: typing.Optional[str] = ...,
        reporting_instance: typing.Optional[str] = ...,
        series: typing.Optional[kubernetes.client.EventsV1EventSeries] = ...,
        type: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> typing.Any: ...
