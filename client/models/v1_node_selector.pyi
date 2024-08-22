import typing

import kubernetes.client

class V1NodeSelector:
    node_selector_terms: list[kubernetes.client.V1NodeSelectorTerm]
    def __init__(self, *, node_selector_terms: list[kubernetes.client.V1NodeSelectorTerm]) -> None: ...
    def to_dict(self) -> typing.Any: ...
