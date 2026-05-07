from app.services.image_service import generate_image


prompt = """
Minimal modern LinkedIn creative.

Professional AI marketing campaign.

Blue and white corporate branding.

Clean typography.

Futuristic AI workspace.

Premium startup aesthetic.
"""

url = generate_image(prompt)

print(url)