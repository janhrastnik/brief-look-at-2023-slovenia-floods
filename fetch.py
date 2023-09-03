from zipfile import ZipFile
import requests
import os.path

# data source: https://podatki.gov.si/dataset/opozorilna-karta-poplav
# we need to fetch three different shapefiles, which display three different levels of flood hazardous areas

def generic_fetch(file_url: str, file_name: str) -> bool:
    """Helper function for fetching flood file data"""

    print("Now fetching " + file_name + " shapefile")

    if os.path.isfile(file_name + ".shp"):
        # we already have the data file, in which case we can just return true now
        print("Found existing " + file_name + " shapefile!")
        return True
    
    # unfortunately, the government site has an expired certificate...
    # so this will throw a warning in our output upon running, but the files are safe
    data = requests.get(file_url, verify=False)
    if data.ok:
        with open(file_name + ".zip", "wb") as F:
            F.write(data.content)

    # this bool will help us check if both required files have been successfully saved
    shx_received = False
    
    # this is the zip file we have downloaded
    # inside are (amongst other files) 2 shapefiles (.shp and .shx), which we need
    # these files represent geospatial data on the map
    with ZipFile(file_name + ".zip") as zip:

        with zip.open(file_name + ".shx") as shapefile:
            with open(file_name + ".shx", "wb") as F:
                res = F.write(shapefile.read())
                if res:
                    print(file_name + ".shx has been successfully fetched and saved!")
                    shx_received = True

        with zip.open(file_name + ".shp") as shapefile:
            with open(file_name + ".shp", "wb") as F:
                res = F.write(shapefile.read())
                if res:
                    print(file_name + ".shp has been successfully fetched and saved!")
                    if shx_received:
                        # both files have been received
                        return True
    return False

def fetch_data() -> bytes:
    """Returns html of the wiki page on the 2023 floods if data was successfully fetched, throws an error otherwise"""

    print("Now fetching the required shapefiles...")

    very_rare = generic_fetch("https://www.statika.evode.gov.si/fileadmin/vodkat/DRSV_OPKP_ZR_POPL.zip", "DRSV_OPKP_ZR_POPL")
    rare = generic_fetch("https://www.statika.evode.gov.si/fileadmin/vodkat/DRSV_OPKP_REDKE_POPL.zip", "DRSV_OPKP_REDKE_POPL")
    common = generic_fetch("https://www.statika.evode.gov.si/fileadmin/vodkat/DRSV_OPKP_POGOSTE_POPL.zip", "DRSV_OPKP_POGOSTE_POPL")

    if very_rare and rare and common:
        # all shapefiles have been fetched and saved!
        # now we fetch html of the wiki page on the 2023 floods 
        print("\nNow fetching info about the floods from wikipedia")

        wiki_html = requests.get("https://en.wikipedia.org/wiki/2023_Slovenia_floods")

        if wiki_html.ok:
            return wiki_html.content
    raise Exception("Something went wrong while fetching data.")
    
