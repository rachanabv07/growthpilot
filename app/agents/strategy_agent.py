def run(state):

    context = state["context"]

    strategy = {
        "platform": "LinkedIn",
        "format": "carousel",
        "tone": context["tone"],
        "post": True
    }

    state["strategy"] = strategy

    return state