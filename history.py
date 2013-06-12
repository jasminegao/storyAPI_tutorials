import requests
import json
import datetime
import settings

query_params = {
    'access_token': settings.ACCESS_TOKEN,
    'story_id': "b966d4d15f38ad3a2b9c40b9cab185a2",
    'filters': ("top10_by_current_rate"),
    'start_time': datetime.timedelta(minutes=10),
    'end_time': datetime.datetime.now()
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/history"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data