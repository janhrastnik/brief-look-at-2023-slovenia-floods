from bs4 import BeautifulSoup
from flood_data import FloodData
from historical_weather_data import HistoricalWeatherData
import requests
import os.path

def handle_historical_weather_data(location, evaled_file) -> HistoricalWeatherData:
    data = evaled_file['data']
    
    temp = []
    wind = []
    solar = []
    rain = []
    
    for entry in data:
        # an entry looks like this: 
        # coords, model name, model elevation, utc offset, temp, wind speed, solar radiation, precipitation

        temp.append(entry[4])
        wind.append(entry[5])
        solar.append(entry[6])
        rain.append(entry[7])

    return HistoricalWeatherData(location, temp, wind, solar, rain)

def analyse_data(wiki_bytes: bytes) -> FloodData:
    """
        Here we collect some data about the flood from the wikipedia article about it.
        We use web scraping via beautifulSoup to receive it.
        Returns a floodData object if everything went ok.
    """

    soup = BeautifulSoup(wiki_bytes, 'html.parser')

    # the web scraping part of code
    title_element = soup.find("caption", class_="infobox-title")
    title = title_element.string

    date_element = soup.find('th', string="Date").parent
    date = date_element.td.string

    location_element = soup.find('th', string="Location").parent
    locations = [location.string for location in location_element.find_all('a')]

    deaths_element = soup.find('th', string="Deaths").parent
    deaths = deaths_element.td.string

    # our flood data object, that will be useful later
    flood_data = FloodData(title, date, locations, deaths)

    # while we are here, let's compare / analyse the sizes of our shapefiles
    common_size = os.path.getsize("DRSV_OPKP_POGOSTE_POPL.shp")
    rare_size = os.path.getsize("DRSV_OPKP_REDKE_POPL.shp")
    very_rare_size = os.path.getsize("DRSV_OPKP_ZR_POPL.shp")

    if common_size < rare_size and rare_size < very_rare_size:
        print("Common floods shapefile is the smallest shapefile, and very rare floods shapefile is the largest one!")

        # note that this a result that we would expect and everything is in order
        # the area of commonly flooded areas should be smaller than the area of very rare floods
        # i.e. we can think of the commonly flooded areas as a subset of the very rare floods
        # and we would expect to see such a result later on the map as well

    # WEATHER DATA
    # here we take a look at historical weather data, for the 4 most flood-exposed areas that we fetched above
    # the data is already fetched, using the 'get_weather_data.py' file

    carinthia_historical = None 
    carniola_historical = None 
    littoral_historical = None 
    styria_historical = None 
    
    with open('fetched_weather_data/carinthia.json', 'r') as F:
        evaled_file = eval(F.read())
        carinthia_historical = handle_historical_weather_data('Carinthia', evaled_file)

    with open('fetched_weather_data/carniola.json', 'r') as F:
        evaled_file = eval(F.read())
        carniola_historical = handle_historical_weather_data('Carniola', evaled_file)

    with open('fetched_weather_data/littoral.json', 'r') as F:
        evaled_file = eval(F.read())
        littoral_historical = handle_historical_weather_data('Slovene Littoral', evaled_file)

    with open('fetched_weather_data/styria.json', 'r') as F:
        evaled_file = eval(F.read())
        styria_historical = handle_historical_weather_data('Styria', evaled_file)

    print("\n - - - Weather reports for 3rd August to 6th August - - - \n")
    
    max_precipitations = []
    
    max_precipitations.append(carinthia_historical.report())
    max_precipitations.append(carniola_historical.report())
    max_precipitations.append(littoral_historical.report())
    max_precipitations.append(styria_historical.report())

    current_max = [0, "foo"]
    for entry in max_precipitations:
        if entry[0] > current_max[0]:
            current_max = entry

    print("\nThe region with the heaviest rainfall was {}\n".format(current_max[1]))
    
    return flood_data
