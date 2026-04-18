from openai import OpenAI
import base64
OpenAI_API = OpenAI()

with open("TestImages/LazerTestImage.jpg", "rb") as testImage:
    imageData = testImage.read()

# --// Format image to form AI can use
formattedImage = base64.b64encode(imageData).decode("utf-8")

def testLazerDim():
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
                        "image_url": f"data:image/jpeg;base64,{formattedImage}"
                    }
                ]
            }
        ]
    )
    print(response.output_text)

"""
def lol():
    print("lol is running")

    firstresponse = OpenAI_API.responses.create(
        model="gpt-5.4",
        instructions="You are a fashion model and you are trying to help people create an instagram post based on a questionnaire that was filled out (assume it already was just have random options)",
        input="based on the answers, you will create an outfit inspiration, a music suggestion, and a caption. Keep answers short and sweet"
    )

    print("response received")
    print(firstresponse.output_text)
"""
