from openai import OpenAI
from InfoModule import appearanceSelection, musicSelection, vibeSelection

def main():

    client = OpenAI()


    response = client.responses.create(
        model="gpt-5.4",
        instructions="You are a fashion model and you are trying to help people create an instagram post based on a questionaire that was filled out( assume it already was just have random options) ",
        input="based on the answers, you will create a outfit inspiration, a music suggestion, and a caption. Basically you will be doing enough to create a blueprint for an instagram post or an instagram story, keep answers short and sweet"
    )



    print(response.output_text)


#calls the main function
if __name__ == "__main__":
    main()