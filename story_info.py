import requests
import json
import settings

query_params = {
    'access_token': settings.ACCESS_TOKEN,
    'link': "http://bit.ly/14eLfvJ"
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/story_info"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data