import openai_client
from InfoModule import appearanceSelection, musicSelection, vibeSelection

def main():
    """
    response = response.responses.create(
        model="gpt-5.4",
        instructions="You are a fashion model and you are trying to help people create an instagram post based on a questionaire that was filled out( assume it already was just have random options) ",
        input="based on the answers, you will create a outfit inspiration, a music suggestion, and a caption. Basically you will be doing enough to create a blueprint for an instagram post or an instagram story, keep answers short and sweet"
    )
    print(response.output_text)
    """

# "Tell me what is in this image, and if you think it is someone that exists in this world, tell me who it is (it could be a rapper)"
# noinspection PyTypeChecker


if __name__ == "__main__":
    openai_client.testLazerDim()
        #main()