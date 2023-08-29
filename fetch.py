from zipfile import ZipFile
import requests
import os.path

# data source: https://podatki.gov.si/dataset/opozorilna-karta-poplav
# we need to fetch three different shapefiles, which display three different levels of flood hazardous areas
# DRSV_OPKP_ZR_POPL

def generic_fetch(file_url: str, file_name: str) -> bool:
    """Helper function for fetching flood file data"""
    print("Now fetching " + file_name + " shapefile")

    if os.path.isfile(file_name + ".shp"):
        # we already have the data file, in which case we can just return true now
        print("Found existing " + file_name + " shapefile!")
        return True
    
    # unfortunately, the government site has an expired certificate...
    data = requests.get(file_url, verify=False)
    if data.ok:
        with open(file_name + ".zip", "wb") as F:
            F.write(data.content)

    shx_received = False
    
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

def fetch_data() -> bool:
    """Returns true if data was successfully fetched, and false if something went wrong"""
    print("Now fetching the required shapefiles")

    return generic_fetch("https://www.statika.evode.gov.si/fileadmin/vodkat/DRSV_OPKP_ZR_POPL.zip", "DRSV_OPKP_ZR_POPL")
