import requests
import json
import uuid
import os
import base64

from app.core.config import OPENROUTER_API_KEY
from app.core.config import BASE_URL

URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_image(prompt: str):

    response = requests.post(
        url=URL,

        headers={
            "Authorization":
                f"Bearer {OPENROUTER_API_KEY}",

            "Content-Type":
                "application/json",
        },

        data=json.dumps({

            "model":
                "bytedance-seed/seedream-4.5",

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            "modalities": ["image"]
        })
    )

    print("STATUS:", response.status_code)

    data = response.json()

    print(data)

    # Extract image
    image_data_url = (
        data["choices"][0]
        ["message"]["images"][0]
        ["image_url"]["url"]
    )

    # Remove base64 header
    base64_image = image_data_url.split(",")[1]

    # Decode
    image_bytes = base64.b64decode(base64_image)

    # Create folder
    os.makedirs("generated", exist_ok=True)

    # Save file
    filename = f"generated/{uuid.uuid4()}.png"

    with open(filename, "wb") as f:
        f.write(image_bytes)

    # Return public URL
    return f"{BASE_URL}/{filename}"