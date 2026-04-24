import urllib.request
import urllib.parse
import re
import json

def search_image(query):
    try:
        url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query + " image thumbnail")
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        # DDG images in html usually are passed in via img src="//duckduckgo.com/iu/?u=..."
        match = re.search(r'//duckduckgo\.com/iu/\?u=([^&"\'\?]+)', html)
        if match:
            return urllib.parse.unquote(match.group(1))
    except Exception as e:
        print(e)
    return "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=400&q=80" # fallback

queries = [
    "Physics Wallah Arjuna JEE 2025 batch",
    "Physics Wallah Lakshya JEE 2025 batch",
    "Physics Wallah Prayas JEE 2025 dropper batch",
    "Physics Wallah Arjuna NEET 2025 class 11 batch",
    "Physics Wallah Lakshya NEET 2025 batch",
    "Physics Wallah Yakeen NEET 2025 batch",
    "Physics Wallah UPSC Sankalp batch",
    "Physics Wallah SSC CGL Mahapack batch",
    "Physics Wallah NDA Shaurya batch",
    "Physics Wallah GATE Parakram batch",
    "Physics Wallah CUET Samarth batch",
    "Physics Wallah CLAT Law batch",
    "Physics Wallah CAT MBA batch",
    "Physics Wallah Banking Mahapack"
]

results = {}
for q in queries:
    results[q] = search_image(q)

print(json.dumps(results, indent=2))
