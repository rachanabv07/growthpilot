from langgraph.graph import StateGraph, END

from app.graph.state import WorkflowState

from app.agents import (
    context_agent,
    strategy_agent,
    content_agent,
    evaluation_agent,
    creative_agent,
    image_agent
)

builder = StateGraph(WorkflowState)

builder.add_node("context", context_agent.run)

builder.add_node("strategy", strategy_agent.run)

builder.add_node("content", content_agent.run)

builder.add_node("evaluation", evaluation_agent.run)

builder.add_node("creative", creative_agent.run)

builder.add_node("image", image_agent.run)

builder.set_entry_point("context")

builder.add_edge("context", "strategy")

builder.add_edge("strategy", "content")

builder.add_edge("content", "evaluation")

MAX_ITERATIONS = 3


def evaluation_router(state):

    approved = state["evaluation"]["approved"]

    iterations = state["iterations"]

    if approved:
        return "creative"

    if iterations >= MAX_ITERATIONS:
        return "creative"

    return "content"

builder.add_conditional_edges(
    "evaluation",
    evaluation_router
)

builder.add_edge("creative", "image")

builder.add_edge("image", END)

graph = builder.compile()