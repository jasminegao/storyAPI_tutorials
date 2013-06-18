storyAPI_tutorials
==================

At bitly, a story is a group of related links that are about the same thing. This is based on shared topics and phrases extracted from the content of each link. On  [rt.ly](http://rt.ly), our realtime search engine, each link has a story page which can be accessed by clicking on the circular 'i' icon.

The following are simple tutorials to help you get started with using bitly's [story APIs](http://dev.bitly.com/story_api.html), which allow you to look at aggregate data for a story or group of related links. For these tutorials we will be using a generic access token generated for the bitlyapitutorials account. To get your own
access token, [click here](https://bitly.com/a/oauth_apps) to generate
one or visit our [OAuth documentation](http://dev.bitly.com/authentication.html) for a walkthrough of the authentication process. 

Listed are tutorials to perform the following:

* Getting the story id for a link or the links from a story id
* Searching for stories
* Getting a story's title
* Returning the metadata of a story
* Seeing a story's distribution
* Looking at a story's historical clickrates

<a id="story_info"></a>Getting the story id for a link or the links from a story id
-------------------------------------------------------------------------------------
To find out what story a bitly link belongs to, you can use the [/v3/story_api/story_info](http://dev.bitly.com/story_api.html#v3_story_api_story_info) endpoint and pass it into `link` parameter:

```python
import requests
import json
import settings

query_params = {
    'access_token': "your_access_token",
    'link': "http://bit.ly/14eLfvJ"
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/story_info"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data
```
The above prints out a JSON response containing the story id, which brings you to the corresponding story page when added to the end of this url: `http://rt.ly/story?story_id=`.

Conversely, you can replace the `link` parameter with a `story_id` parameter if you already have the id for a story and want to find the associated links.  

<a id="phrases"></a>Searching for stories
--------------------------------------------------------------------------------
You can also search for stories as you would links on [rt.ly](http://rt.ly) by querying with keywords or phrases. To find stories about the riots in Istanbul, for example, connect to the [/v3/story_api_story_from_phrases](http://dev.bitly.com/story_api.html#v3_story_api_story_from_phrases) endpoint and pass your search term(s) into the `phrases` parameter:

```python
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
```

This search will return the a list of recent links related to the `phrases` "istanbul, "gezi park" and "turkey" and the corresponding `story id` for those links. 


<a id="title"></a>Getting a story's title
--------------------------------------------------------------------------------
Given a story id or link(s), the [/v3/story_api/title](http://dev.bitly.com/story_api.html#v3_story_api_title) endpoint can be used to return the most representative title:

```python
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
```    

<a id="metadata"></a>Returning the metadata of a story
--------------------------------------------------------------------------------
We can get back even more specific data for a given story id or link(s) by using the [/v3/story_api/metadata](http://dev.bitly.com/story_api.html#v3_story_api_metadata) endpoint and specifying what `field`s we want returned:

```python
import requests
import json
import settings

query_params = {
    'access_token': "your_access_token",
    'story_id': "b966d4d15f38ad3a2b9c40b9cab185a2",
    'field': ("rates", "titles", "images", "clicks")
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/metadata"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data
```

The above code returns the current click `rates` of the story, a list of page `titles` for the links contained in that story, a list of `images` extracted from those links and the total number of `clicks` on the story. Additional fields that may also be returned are `related`, which gives back a list of related pages, `shares`, the number of times the story has been shared, and `encoders`, the number of times the story has been shortened.  

<a id="distribution"></a>Seeing a story's distribution
--------------------------------------------------------------------------------------
Each story is distributed and consumed in a unique way. We can see, for example, where on the internet a story is receiving its clicks as well as where, geographically, in the world those clicks are originating from. This can be done using the [/v3/story_api/distribution](http://dev.bitly.com/story_api.html#v3_story_api_distribution) endpoint and, like with the metadata endpoint, specifying which distributions we want returned in the `field`:

```python
import requests
import json
import settings

query_params = {
    'access_token': "your_access_token",
    'story_id': "b966d4d15f38ad3a2b9c40b9cab185a2",
    'limit': 10,
    'field': ("cities", "domains", "referrers")
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/distribution"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data
```

Here, given a story id, we `limit` the results to 10 for each `field` and get back the top 10 cities from which the story is receiving clicks, domains on which links in the story appear, and link referrers. You can also return a more general distribution across `regions` and `countries` as well as get back associated `phrases` and `topics`. 


<a id="history"></a>Looking at a story's historical clickrates
--------------------------------------------------------------------------------
On top of the distribution data for a story, we can also look at the historical clickrates using the [/v3/story_api/history](http://dev.bitly.com/story_api.html#v3_story_api_history) endpoint:

```python 
import requests
import json
import datetime
import settings

query_params = {
    'access_token': "your_access_token",
    'story_id': "b966d4d15f38ad3a2b9c40b9cab185a2",
    'filters': ("top10_by_current_rate"),
    'start_time': datetime.timedelta(minutes=10),
    'end_time': datetime.datetime.now()
}

endpoint = "https://api-ssl.bitly.com/v3/story_api/history"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data
```

In this example, passing `top10_by_current_rate` into the `filters` parameter gives us back the clickrate history for the story as a whole as well as the individual histories for the top 10 links in that story. The time period we are returning clickrates for is during the last 10 minutes as specified by the `start_time` and `end_time` parameters, which take unix timestamps (though we've avoided that by using the `datetime` library). 

Additional `filters` that can be used are `merged`, which returns the clickrate history of a story as a whole, and `all`, which returns the individual histories for every link in the story.  
