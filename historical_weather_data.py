import statistics

class HistoricalWeatherData:
    """Stores historical weather data about a particular location"""

    def __init__(
        self, 
        location: str, 
        temperature: list[int], 
        wind_speed: list[int],
        solar_radiation: list[int],
        precipitation: list[int]
    ):
        self.location = location
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.solar_radiation = solar_radiation
        self.precipitation = precipitation

    def report(self):
        """
            Logs general info and some calculations about the weather data into the console.
            Returns list of 2 items: [max_precipitation, location]
        """

        print("\nWEATHER REPORT FOR {location}\n".format(location=self.location))
        
        # first, let's look at the temperature
        print("Largest reached temperature: {} Celsius".format(round(max(self.temperature), 2)))
        print("Minimum reached temperature: {} Celsius".format(round(min(self.temperature), 2)))
        print("Mean temperature: {} Celsius".format(round(statistics.mean(self.temperature), 2)))

        # now wind speed, here only max is really interesting...
        print("\nLargest reached wind speed: {} m/s".format(max(self.wind_speed)))

        # solar radiation (eli5: how much sun hits the ground)
        # it makes sense to look at the mean here
        print("\nMean radiation: {} Watt / metres squared".format(round(statistics.mean(self.solar_radiation), 2)))

        # precipitation, this is the key area we are interested in!
        # explanation of what the heck this means: https://earthscience.stackexchange.com/questions/14587/what-does-a-mm-of-rain-mean
        print("\nLargest reached precipitation: {} mm".format(round(max(self.precipitation), 2)))
        print("Mean precipitation: {} mm".format(round(statistics.mean(self.precipitation), 2)))

        return [round(max(self.precipitation), 2), self.location]
        
