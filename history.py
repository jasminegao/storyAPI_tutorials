import requests
import json
import datetime
import settings

query_params = {
    'access_token': settings.ACCESS_TOKEN,
    'story_id': "76972ebca282673ae0eac65bb1ed393c",
    'filters': ("top10_by_current_rate"),
    'start_time': datetime.timedelta(minutes=10),
    'end_time': datetime.datetime.now()
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/history"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data