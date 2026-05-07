from app.services.image_prompt_service import build_image_prompt
from app.services.image_service import generate_image


def run(state):

    content = state["content"]
    creative = state["creative"]

    image_prompt = build_image_prompt(content, creative)

    image_url = generate_image(image_prompt)

    state["image"] = {
        "prompt": image_prompt,
        "url": image_url
    }

    return state