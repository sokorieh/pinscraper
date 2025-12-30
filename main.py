import requests
import re
import os
import time

BOARD_URL = "https://pin.it/xyz" # replace the link with your board's url
OUT_DIR = "pinterest_images"

os.makedirs(OUT_DIR, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(BOARD_URL, headers=headers).text

urls = set(re.findall(r'https://i\.pinimg\.com/[^"]+\.jpg', html))

def upscale(url):
    return re.sub(r'/\d+x/', '/originals/', url)

for i, url in enumerate(urls):
    img_url = upscale(url)
    img_data = requests.get(img_url, headers=headers).content

    with open(f"{OUT_DIR}/{i}.jpg", "wb") as f:
        f.write(img_data)

    time.sleep(0.5)  
