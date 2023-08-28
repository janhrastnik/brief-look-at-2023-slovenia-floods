from zipfile import ZipFile
import requests
import os.path

# data source info: https://podatki.gov.si/dataset/opozorilna-karta-poplav
# url to data source: https://www.statika.evode.gov.si/fileadmin/vodkat/DRSV_OPKP_ZR_POPL.zip

def fetch_data() -> bool:
    """returns true if data was successfully fetched, and false if something went wrong"""
    print("Now fetching the required shapefile data")

    if os.path.isfile("data.shp"):
        # we already have the data file, in which case we can just return true now
        print("Found existing 'data.shp' file!")
        return True
    
    # unfortunately, the government site has an expired certificate...
    data = requests.get("https://www.statika.evode.gov.si/fileadmin/vodkat/DRSV_OPKP_ZR_POPL.zip", verify=False)
    if data.ok:
        with open("data.zip", "wb") as F:
            F.write(data.content)

    with ZipFile("data.zip") as zip:
        with zip.open("DRSV_OPKP_ZR_POPL.shp") as shapefile:
            with open("data.shp", "wb") as F:
                res = F.write(shapefile.read())
                if res:
                    print("'data.shp' has been successfully fetched and saved!")
                    return True
    return False
