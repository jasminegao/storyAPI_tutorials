import requests
import json
import settings

query_params = {
    'access_token': "your_access_token",
    'phrases': ("istanbul", "gezi park", "turkey")
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/story_from_phrases"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data