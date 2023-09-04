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

    def max_precipitation(self) -> int:
        return max(self.precipitation)
