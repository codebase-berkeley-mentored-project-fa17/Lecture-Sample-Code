import requests
import json

consumer_key = 'Sxtc7BNdLj5VA3dpg3oLwzqbRTQzy4Mj'
consumer_secret = ' VYKOvBsWcO1dEcz7'

URL = "http://www.mapquestapi.com/geocoding/v1/address?key=" + consumer_key + "&location=67+Ottowa+Road+South+Marlboro+NJ"
PARAMS = {}
response = requests.get(url=URL, params=PARAMS)

obj = json.loads(response.text)
print(obj['results'][0]['locations'][0]['latLng']['lat'])