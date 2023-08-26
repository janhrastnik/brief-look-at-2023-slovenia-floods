import urllib.request

# data source info: https://podatki.gov.si/dataset/surs0711335s
# url to data source: https://pxweb.stat.si/SiStatData/Resources/PX/Databases/Data/0711335S.PX

with urllib.request.urlopen("https://pxweb.stat.si/SiStatData/Resources/PX/Databases/Data/0711335S.PX") as F:
    content = F.read()
    print(content)
