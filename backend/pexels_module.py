from xml.etree.ElementTree import tostring

import requests

API_KEY = "Idf81fua0DBkxBjXozcUhfY4dLjFTaXAOH8VTpM4MQdUUBkuuotxXiNx"

headers = {
    "Authorization": API_KEY
}

url = "https://api.pexels.com/v1/search?query=streetwear outfit&per_page=5"

def search_images(query, limit=5):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={limit}"
    r = requests.get(url, headers=headers)
    return r.json()

imageurls = []
image_info = search_images("male confident streetwear outfit")
for photo in image_info["photos"]:
    imageurls.append(photo["src"]["original"])


print(imageurls)