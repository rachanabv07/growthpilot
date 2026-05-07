def run(state):

    event = state["event"]

    if "day" in event.lower():
        event_type = "celebration"
    else:
        event_type = "corporate"

    state["context"] = {
        "event_type": event_type,
        "tone": "professional",
        "audience": "linkedin professionals"
    }

    return state