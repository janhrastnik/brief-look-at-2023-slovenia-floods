from fetch import fetch_data
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

res = fetch_data()
if res:
    display_data()

