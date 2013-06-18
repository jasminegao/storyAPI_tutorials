import requests
import json
import settings

query_params = {
    'access_token': "your_access_token",
    'story_id': "b966d4d15f38ad3a2b9c40b9cab185a2"
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/title"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data
