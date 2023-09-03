import geopandas
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from flood_data import FloodData

def display_data(flood_data: FloodData):
    """
        Displays a matplotlib plot, that contains an outline of Slovenia, and the 3 flood regions that we fetch from the government
        Also logs some info about the 2023 floods into the console.
    """

    print("\n - - - Some info about the {title} - - -".format(title=flood_data.title))
    print("It took place on {date}".format(date=flood_data.date))
    print("Main flooding locations were in {locations}".format(locations=flood_data.format_locations()))
    print("At least {deaths} casualties happened due to these floods".format(deaths=flood_data.deaths))

    fig, ax = plt.subplots()

    fig.suptitle('Areas of different flood severity')

    slovenia = geopandas.read_file("assets/P250V7000_pF.shp")
    slovenia.plot(ax=ax)

    very_rare = geopandas.read_file("DRSV_OPKP_ZR_POPL.shp")
    line = very_rare.plot(ax=ax, color="green", zorder=0)

    rare = geopandas.read_file("DRSV_OPKP_REDKE_POPL.shp")
    rare.plot(ax=ax, color="red", zorder=1)

    common = geopandas.read_file("DRSV_OPKP_POGOSTE_POPL.shp")
    common.plot(ax=ax, color="black", zorder=2)

    very_rare_patch = mpatches.Patch(color='green', label='Very rare flooding')
    rare_patch = mpatches.Patch(color='red', label='Rare flooding')
    common_patch = mpatches.Patch(color='black', label='Common flooding')
    ax.legend(handles=[very_rare_patch, rare_patch, common_patch], loc="upper left")

    plt.show()