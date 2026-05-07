import json

from app.services.llm_service import generate_content


def run(state):

    content = state["content"]

    prompt = f"""
You are a creative director for LinkedIn brand campaigns.

Create a visual strategy for this LinkedIn post.

Post:
{json.dumps(content, indent=2)}

Return ONLY valid JSON:

{{
  "visual_style": "...",
  "color_theme": "...",
  "layout": "...",
  "image_type": "...",
  "visual_elements": ["...", "..."]
}}
"""

    response = generate_content(prompt)

    try:
        parsed = json.loads(response)
    except:
        parsed = {
            "visual_style": "minimal",
            "color_theme": "blue",
            "layout": "centered",
            "image_type": "linkedin post",
            "visual_elements": ["professional workspace"]
        }

    state["creative"] = parsed

    return state