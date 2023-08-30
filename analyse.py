from bs4 import BeautifulSoup
from flood_data import FloodData
import requests
import os.path

def analyse_data() -> FloodData:
    """
        Here we collect some data about the flood from the wikipedia article about it.
        We use web scraping via beautifulSoup to receive it.
        Returns a floodData object if everything went ok.
    """

    print("\nNow fetching info about the floods from wikipedia")

    wiki_html = requests.get("https://en.wikipedia.org/wiki/2023_Slovenia_floods")

    if not wiki_html.ok:
        return False
    
    soup = BeautifulSoup(wiki_html.content, 'html.parser')

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
    flood_data = FloodData(title, date, locations, deaths);

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
    
    return flood_data
