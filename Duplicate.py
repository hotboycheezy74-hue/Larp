import re
from openai import OpenAI

client = OpenAI()
vibe = "streetwear"

def build_pinterest_query(text, vibe):
    cleaned = text.lower()
    cleaned = re.sub("[^a-z0-9 ]", "", cleaned)

    keywords = [
        "hoodie", "cargo", "cargos", "jeans", "dress", "jacket",
        "sneakers", "heels", "boots", "blazer", "skirt", "graphic",
        "oversized", "streetwear", "casual", "chill", "sporty"
    ]

    found = [word for word in keywords if word in cleaned]

    if found:
        return vibe + " outfit " + " ".join(found[0:3])
    words = cleaned.split()
    return vibe + " outfit " + " ".join(words[:5])


response = client.responses.create(
    model="gpt-5.4",
    instructions=(
        "You are a fashion model and you are trying to help people create "
        "an Instagram post based on a questionnaire that was filled out. "
        "Assume the questionnaire was already filled out with random options."
    ),
    input=(
        f"The selected vibe is {vibe}. "
        "Based on the answers, create an outfit inspiration, a music suggestion, "
        "and a caption. Keep answers short and sweet."
    )
)

text = response.output_text
pinterest_query = build_pinterest_query(text, vibe)

print("OpenAI Output:\n")
print(text)

print("\nPinterest Query:\n")
print(pinterest_query)
