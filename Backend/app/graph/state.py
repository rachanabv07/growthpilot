from typing import TypedDict


class WorkflowState(TypedDict, total=False):

    event: str
    note: str

    iterations: int

    context: dict
    strategy: dict
    content: dict
    evaluation: dict
    creative: dict
    image: dict