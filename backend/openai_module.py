import base64

import InfoModule
from openai import OpenAI

OpenAI_API = OpenAI()

def ai_request(promptstring, formattedimage=None):
    if formattedimage is None:
        response = OpenAI_API.responses.create(
            model="gpt-5.4",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": promptstring
                        }
                    ]
                }
            ]
        )
    else:
        response = OpenAI_API.responses.create(
            model="gpt-5.4",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": promptstring
                        },
                        {
                            "type": "input_image",
                            "image_url": f"data:image/jpeg;base64,{formattedimage}"
                        }
                    ]
                }
            ]
        )

    return response

def get_image_vibe(image_path):
    promptstring = (
        f"Analyze this photo and output one single word that matches the image "
        f"from this list of vibes: {InfoModule.vibeSelection}. "
        f"Do not give any extra text. Only output the exact single word."
    )

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    formattedimage = base64.b64encode(image_data).decode("utf-8")
    response = ai_request(promptstring, formattedimage)

    return response.output_text

def get_outfit_style(image_path):
    promptstring = (
        f"Analyze this photo and output 1 singular word from each of these 3 lists "
        f"{InfoModule.appearanceSelection} in this format: Style: x, Palette: y, Presentation: z"
    )

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    formattedimage = base64.b64encode(image_data).decode("utf-8")
    response = ai_request(promptstring, formattedimage)

    return response.output_text

def generate_caption(inputdata):
    promptstring = f"""
    Create 3 Instagram captions based on the following input:
    Photo Vibe: {inputdata["Photo Vibe"]}
    Music Genre: {inputdata["Music Genre"]}
    Music Energy: {inputdata["Music Energy"]}
    Music Era: {inputdata["Music Era"]}
    Music Artist: {inputdata["Music Artist"]}
    Appearance Style: {inputdata["Appearance Style"]}
    Appearance Presentation: {inputdata["Appearance Presentation"]}

    Requirements:
    - Sound natural and modern
    - No cringe or corny lines
    - Short to medium length
    - Match Gen Z / current Instagram tone
    - Some captions subtle, some confident
    - Include one with an emoji
    - Include one with a one-liner
    - Include one with a flex caption
    """

    response = ai_request(promptstring)
    return response.output_text