🌊 🇸🇮
# A brief look at the 2023 Slovenia floods 
This is a project, made for the 'Uvod v programiranje' class at FMF. It examines, which areas in Slovenia are more susceptible to flooding, 
and compares these areas to the ones that were actually flooded in the 2023 Slovenia floods. We use Python 3 + some external libraries to achieve this goal.

## How it works
We first fetch some data from a government-backed dataset, which you can find more about [here](https://podatki.gov.si/dataset/opozorilna-karta-poplav).
From this dataset, we get shapefiles, that represent areas of different levels of flood severity. These shapefiles contain geospatial data, which you
can draw using an appropriate library. Here we use [geopandas](https://geopandas.org/en/stable/) for that matter.

We then gather some info about the 2023 floods, by web-scraping the wiki article of it (which you can find [here](https://en.wikipedia.org/wiki/2023_Slovenia_floods)).
For this task we use BeautifulSoup, the de facto standard for web scraping in Python.

We then draw plots, that show maps of Slovenia with these areas, by using geopandas and matplotlib. Using a pdf, that shows how the 2023 floods took place, we can then
compare our event of 2023 floods with the historical areas of flooding in Slovenia.

## How to run
The project uses multiple non-standard Python libraries, which you will have to install in order to run the project.
Install them quickly with the following command:\
<code>pip install -r requirements.txt</code>\
, where the <code>requirements.txt</code> file contains a list of required python libraries.\
<em>I would also recommend, from personal experience, using a virtual enviroment to install these dependencies and run this project. Managing a plethora of libraries
on a whole system globally is not advisable.</em>

You can then run the project with:\
<code>python main.py</code>

This will download the required shapefiles, and display a plot of Slovenia, with different areas of flood severity.

Once you've done all that, you can open the Jupyter notebook <code>report.ipynb</code>, in whichever feasible way of doing that, that is up to your liking.
The Jupyter notebook contains a report on the project, with additional explanations and examples of how the project works.

## Contributions
Any issues / pull requests, that address any bugs / typos that may be present in the project, are much appreciated.
