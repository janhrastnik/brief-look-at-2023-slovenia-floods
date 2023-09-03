import requests
import json

"""
    This file fetches historical weather data.
    More specifically, we get data associated with the 2023 floods in Slovenia.
    You need to pass in an API key from weatherstack to run this file.
"""

api_key = "We set the API key in this variable"

# you must get your own key from weatherstack, should you want to run this code
with open("apikey.txt", "r") as F:
    api_key = F.read()

url = 'https://api.oikolab.com/weather'

locations = "Slovene Littoral, Upper Carniola, Carinthia, Styria"
dates = "2023-08-03;2023-08-04;2023-08-05;2023-08-06"

params = {'param': 'temperature',
    'location': 'Slovene Littoral, Slovenia',
    'start': '2023-08-03',
    'end': '2023-08-06'}

headers = {'api-key': api_key}

res = requests.get(url, params=params, headers=headers)

if res.ok:
    evaled_text = eval(res.text)
    data = evaled_text['data']
    evaled_data = eval(data)
    with open("fetched_weather_data/littoral.json", "w") as F:
        json.dump(evaled_data, F)