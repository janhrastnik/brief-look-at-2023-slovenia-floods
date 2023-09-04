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

headers = {'api-key': api_key}

def generic_params(location: str):
    return {
        'param': ['temperature', 'wind_speed', 'surface_solar_radiation', 'total_precipitation'],
        'location': location,
        'start': '2023-08-03',
        'end': '2023-08-06'
    }

def generic_call(location: str, filename: str):
    params = generic_params(location)

    res = requests.get(url, params=params, headers=headers)

    if res.ok:
        evaled_text = eval(res.text)
        data = evaled_text['data']
        evaled_data = eval(data)
        with open("fetched_weather_data/{filename}".format(filename=filename), "w") as F:
            json.dump(evaled_data, F)
            print("Saved {filename}".format(filename=filename))
    else:
        print(res.reason)

generic_call('Primorska, Slovenija', 'littoral.json')
generic_call('Gorenjska, Slovenija', 'carniola.json')
generic_call('Koroška, Slovenija', 'carinthia.json')
generic_call('Štajerska, Slovenija', 'styria.json')
