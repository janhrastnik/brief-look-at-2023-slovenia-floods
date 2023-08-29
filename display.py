import geopandas
import matplotlib.pyplot as plt

def display_data():

    fig, ax = plt.subplots()

    slovenia = geopandas.read_file("assets/P250V7000_pF.shp")
    slovenia.plot(ax=ax)

    common = geopandas.read_file("DRSV_OPKP_ZR_POPL.shp")
    common.plot(ax=ax, color="green")

    common = geopandas.read_file("DRSV_OPKP_REDKE_POPL.shp")
    common.plot(ax=ax, color="red")

    common = geopandas.read_file("DRSV_OPKP_POGOSTE_POPL.shp")
    common.plot(ax=ax, color="black")

    plt.show()