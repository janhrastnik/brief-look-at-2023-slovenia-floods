class FloodData:
    """Stores data about a particular flood that has happened"""
    
    def __init__(self, title: str, date: str, locations: list, deaths: int):
        self.title = title
        self.date = date
        self.locations = locations
        self.deaths = deaths

    def format_locations(self):
        return " ".join(self.locations)

    def __repr__(self):
        return self.title + ", " + self.date
