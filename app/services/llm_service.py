import requests

from app.core.config import OPENROUTER_API_KEY

URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_content(prompt: str):

    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "x-ai/grok-3-mini-beta",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    data = response.json()
    print(data)

    return data["choices"][0]["message"]["content"]