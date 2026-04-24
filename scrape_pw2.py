import requests
import re
import json

url = "https://pw.live/study/batches"
headers = {"User-Agent": "Mozilla/5.0"}
resp = requests.get(url, headers=headers)

# Let's extract json inside Next.js <script id="__NEXT_DATA__">
match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    batches = []
    # traverse data to find images or batches
    print("Found Next_DATA")
    with open('pw.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
else:
    print("Next data not found")

