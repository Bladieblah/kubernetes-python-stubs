import typing
from urllib3 import BaseHTTPResponse

import kubernetes.client

class V1WeightedPodAffinityTerm:
    pod_affinity_term: kubernetes.client.V1PodAffinityTerm
    weight: int
    def __init__(self, *, pod_affinity_term: kubernetes.client.V1PodAffinityTerm, weight: int) -> None: ...
    def to_dict(self) -> typing.Any: ...
