import geopandas
import matplotlib.pyplot as plt

def display_data():

    fig, ax = plt.subplots()

    slovenia = geopandas.read_file("meje/P250V7000_pF.shp")
    #slovenia = slovenia.scale(0.2, 0.2)
    slovenia.plot(ax=ax)

    thing = geopandas.read_file("data.shp")
    #thing.plot(ax=ax, color="black")

    plt.show()