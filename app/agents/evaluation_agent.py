from app.services.llm_service import generate_content
import json

def run(state):

    content = state["content"]

    formatted = f"""
        Hook:
        {content['hook']}

        Body:
        {content['body']}

        """

    prompt = f"""
You are evaluating a LinkedIn post.

Evaluate the following post based on:

1. Hook strength
2. Professional tone
3. Engagement potential
4. Clarity
5. Brand alignment

Return ONLY valid JSON in this format:

{{
  "score": 0,
  "feedback": "...",
  "approved": score >= 7
  
}}

Post:
{formatted}
"""

    response = generate_content(prompt)

    try:
        parsed = json.loads(response)

    except Exception as e:
        print("JSON PARSE ERROR:", e)
        parsed = {
        "score": 0,
        "feedback": "Retry"
        }

    # try:
    #     score = float(response.strip())
    # except:
    #     score = 5.0

    state["evaluation"] = parsed

    return state