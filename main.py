from fetch import fetch_data
from analyse import analyse_data
from display import display_data

"""
    Main file that runs the project.
    The project is split into 3 parts:
        1. Fetching the data 
        2. Analysing the data
        3. Displaying the data
"""

print("\n~~~~~~~~~~~~~~~~")
print("~ The Project™ ~")
print("~~~~~~~~~~~~~~~~\n")

if fetch_data():
    flood_data = analyse_data()
    if flood_data:
        display_data()

