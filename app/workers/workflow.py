# from app.agents import (
#     context_agent,
#     strategy_agent,
#     content_agent,
#     evaluation_agent
# )
# from app.agents import creative_agent
# from app.agents import image_agent

# MAX_ITERATIONS = 3


# def run_workflow(input_data):

#     state = {
#         "event": input_data["event"],
#         "note": input_data["note"],
#         "iterations": 0
#     }

#     state = context_agent.run(state)

#     state = strategy_agent.run(state)

#     while state["iterations"] < MAX_ITERATIONS:

#         state = content_agent.run(state)

#         state = evaluation_agent.run(state)

#         score = state["evaluation"]["score"]

#         print(f"Iteration {state['iterations']} Score: {score}")

#         if score >= 7:
#             break

#     state = creative_agent.run(state)

#     state = image_agent.run(state)

#     return state


from app.graph.builder import graph


def run_workflow(input_data):

    initial_state = {
        "event": input_data["event"],
        "note": input_data["note"],
        "iterations": 0
    }

    result = graph.invoke(initial_state)

    return result