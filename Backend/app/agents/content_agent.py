from app.services.llm_service import generate_content
from pydantic import BaseModel
from typing import List
import json


class LinkedInPost(BaseModel):
    hook: str
    body: str
    cta: str
    hashtags: List[str]

def run(state):

    event = state["event"]
    note = state["note"]
    feedback = state.get("feedback", "")

    prompt = f"""
You are a professional LinkedIn content strategist.

Generate a LinkedIn post for NimbleWork.
Previous feedback:
{feedback}

Event: {event}

Context:
{note}

Return ONLY valid JSON in this format:

{{
  "hook": "...",
  "body": "...",
  "hashtags": ["...", "..."]
}}

Requirements:
- professional tone
- engaging
- concise

"""

    response = generate_content(prompt)

    try:
        parsed = json.loads(response)

    except Exception as e:
        print("JSON PARSE ERROR:", e)

        parsed = {
            "hook": "Fallback Hook",
            "body": response,
            "cta": "Learn more.",
            "hashtags": ["#NimbleWork"]
        }

    state["content"] = parsed


    state["iterations"] += 1

    return state