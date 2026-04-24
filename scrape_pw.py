import requests
import re

url = "https://pw.live/study/batches"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
html = response.text

# Find image URLs
images = re.findall(r'https://[^\s"\'<>]+(?:jpg|jpeg|png|webp)', html)
unique_images = list(set(images))

for img in unique_images[:20]:
    print(img)
