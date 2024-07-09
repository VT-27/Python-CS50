import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
o = response.json()
print(json.dumps(response.json(), indent=2))
for result in o["results"]:
    print(result["artistName"])