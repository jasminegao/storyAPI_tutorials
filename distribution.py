import requests
import json
import settings

query_params = {
    'access_token': settings.ACCESS_TOKEN,
    'story_id': "76972ebca282673ae0eac65bb1ed393c",
    'limit': 10,
    'field': ("cities", "domains", "topics")
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/distribution"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data