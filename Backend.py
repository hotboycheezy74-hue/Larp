from openai import OpenAI
import base64
OpenAI_API = OpenAI()
from InfoModule import appearanceSelection, musicSelection, vibeSelection

# --// Import test image of lazer dim 700
with open("TestImages/LazerTestImage.jpg", "rb") as testImage:
    imageData = testImage.read()

# --// Format image to form AI can use
formattedImage = base64.b64encode(imageData).decode("utf-8")

def main():
    response = OpenAI_API.responses.create(
        model="gpt-5.4",
        instructions="You are a fashion model and you are trying to help people create an instagram post based on a questionaire that was filled out( assume it already was just have random options) ",
        input="based on the answers, you will create a outfit inspiration, a music suggestion, and a caption. Basically you will be doing enough to create a blueprint for an instagram post or an instagram story, keep answers short and sweet"
    )
    print(response.output_text)

# "Tell me what is in this image, and if you think it is someone that exists in this world, tell me who it is (it could be a rapper)"
# noinspection PyTypeChecker
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

#calls the main function
if __name__ == "__main__":
    testLazerDim()
    #main()