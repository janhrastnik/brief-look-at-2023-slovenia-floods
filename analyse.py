from bs4 import BeautifulSoup
import requests

def analyse_data() -> bool:
    """
        Here we collect some data about the flood from the wikipedia article about it.
        We use web scraping via beautifulSoup to receive it.
        Returns true if everything went ok.
    """

    print("\nNow fetching info about the floods from wikipedia")

    wiki_html = requests.get("https://en.wikipedia.org/wiki/2023_Slovenia_floods")

    if not wiki_html.ok:
        return False
    
    soup = BeautifulSoup(wiki_html.content, 'html.parser')

    title_element = soup.find("caption", class_="infobox-title")
    title = title_element.string

    date_element = soup.find('th', string="Date").parent
    date = date_element.td.string

    location_element = soup.find('th', string="Location").parent
    locations = [location.string for location in location_element.find_all('a')]

    deaths_element = soup.find('th', string="Deaths").parent
    deaths = deaths_element.td.string

    return True
