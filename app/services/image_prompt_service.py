def build_image_prompt(content, creative):

    return f"""
Create a premium LinkedIn marketing creative.

STYLE:
{creative['visual_style']}

COLOR THEME:
{creative['color_theme']}

LAYOUT:
{creative['layout']}

VISUAL ELEMENTS:
{", ".join(creative['visual_elements'])}

MAIN MESSAGE:
{content['hook']}

DESIGN REQUIREMENTS:
- modern startup aesthetic
- clean typography
- premium SaaS branding
- professional corporate feel
- highly polished
- suitable for LinkedIn marketing
- visually minimal
- cinematic lighting
- high-end UI/UX style

OUTPUT:
high quality social media campaign creative
"""