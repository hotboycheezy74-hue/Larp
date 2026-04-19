from openai import OpenAI
import InfoModule
import base64
OpenAI_API = OpenAI()

def ai_request(promptstring, formattedimage):
    if not formattedimage:
        response = OpenAI_API.responses.create(
            model = "gpt-5.4",
            input = [
                {
                    "role": "user",
                    "content": [
                        { # --// Text prompt
                            "type": "input_text",
                            "text": promptstring
                        },
                    ]
                }
            ]
        )
    else:
        response = OpenAI_API.responses.create(
            model = "gpt-5.4",
            input = [
                {
                    "role": "user",
                    "content": [
                        { # --// Text prompt
                            "type": "input_text",
                            "text": promptstring
                        },
                        { # --// Image input
                            "type": "input_image",
                            "image_url": f"data:image/jpeg;base64,{formattedimage}" #image should be from inputdata
                        }
                    ]
                }
            ]
        ) # --// Clean up this nasty code later
    return response

def get_image_vibe():
    promptstring = f"Analyze this photo output a word that the image matches the closes out of all of these vibes: {InfoModule.vibeSelection}, Don't give any other text other than the exact single word."
    # --// Image should be a part of the inputdata dict
    with open("TestImages/jordancarter.jpg", "rb") as testImage:
        imagedata = testImage.read(); formattedimage = base64.b64encode(imagedata).decode("utf-8")

    response = ai_request(promptstring, formattedimage)
    print(response.output_text)

def get_outfit_appearance():
    promptstring = f"Analyze this photo output 1 singular word from each of these 3 lists {InfoModule.appearanceSelection} in this format Style: x, Palette: y, Presentation: z"
    with open("TestImages/LazerTestImage.jpg", "rb") as testImage:
        imagedata = testImage.read(); formattedimage = base64.b64encode(imagedata).decode("utf-8")

    response = ai_request(promptstring, formattedimage)
    print(response.output_text)

def generate_caption(inputdata):
    promptstring = f"""
    Create 3 Instagram captions based on the following input:
    Photo Vibe: {inputdata["Photo Vibe"]}
    Music Genre: {inputdata.Music.Genre}
    Music Energy: {inputdata.Music.Energy}
    Music Era: {inputdata.Music.Era}
    Music Artist: {inputdata.Music.Artist or ""}
    Appearance Style: {inputdata["Photo Appearance"]["Style"]}
    Appearance Presentation: {inputdata["Photo Appearance"]["Presentation"]}
    # --// AND THE IMAGE IF INPUTTED
    
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
    response = ai_request(promptstring, False)
    print(response.output_text)
