import requests

API_KEY = "Idf81fua0DBkxBjXozcUhfY4dLjFTaXAOH8VTpM4MQdUUBkuuotxXiNx"

headers = {
    "Authorization": API_KEY
}

url = "https://api.pexels.com/v1/search?query=streetwear outfit&per_page=5"

def search_images(UserInfo, limit=3):
    search_string = f"{UserInfo["Photo Appearance"]["Style"]} {UserInfo["Photo Appearance"]["Presentation"]} {UserInfo["Photo Vibe"]} Outfit"
    url = f"https://api.pexels.com/v1/search?query={search_string}&per_page={limit}"
    r = requests.get(url, headers=headers)
    image_info = r.json()

    imageurls = []
    for photo in image_info["photos"]:
        imageurls.append(photo["src"]["original"])
    return imageurls
