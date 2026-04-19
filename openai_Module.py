from openai import OpenAI
import InfoModule
import base64
OpenAI_API = OpenAI()

def getimageinfo():
    promptstring = f"Analyze this photo output a word that the image matches the closes out of all of these vibes: {InfoModule.vibeSelection}, Don't give any other text other than the exact single word."
    # --// Image should be a part of the inputdata dict
    with open("TestImages/jordancarter.jpg", "rb") as testImage:
        imagedata = testImage.read()

    # --// Format image to form AI can use
    formattedimage = base64.b64encode(imagedata).decode("utf-8")

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
    )
    print(response.output_text)

def backendtest(inputdata):
    promptstring = f"""
    Create 3 Instagram captions based on the following input:
    Photo Vibe: {inputdata["Photo Vibe"]}
    Music Energy: {inputdata["Music Energy"]}
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
                        "image_url": f"data:image/jpeg;base64,{5}" #image should be from inputdata
                    }
                ]
            }
        ]
    )
    print(response.output_text)

def lazerdimtest(inputdata):
    # --// Image should be a part of the inputdata dict
    with open("TestImages/LazerTestImage.jpg", "rb") as testImage:
        imagedata = testImage.read()

    # --// Format image to form AI can use
    formattedimage = base64.b64encode(imagedata).decode("utf-8")
    response = OpenAI_API.responses.create(
        model= "gpt-5.4",
        input = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Analyze this photo and tell me what or who you see, and go into detail."
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{formattedimage}"
                    }
                ]
            }
        ]
    )
    print(response.output_text)

def test():
    response = OpenAI_API.responses.create(
        model="gpt-5.4",
        instructions="You are a fashion model and you are trying to help people create an instagram post based on a questionaire that was filled out( assume it already was just have random options) ",
        input="based on the answers, you will create a outfit inspiration, a music suggestion, and a caption. Basically you will be doing enough to create a blueprint for an instagram post or an instagram story, keep answers short and sweet"
    )
    print(response.output_text)
