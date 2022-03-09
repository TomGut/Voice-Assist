from datetime import datetime

from geopy import Nominatim
from pyowm import OWM


class Weather_Skill:
    # OpenWeather API key
    api_key = "your OpenWeather API key here"

    def __init__(self, city=None) -> None:
        self.ow = OWM(self.api_key)
        self.mgr = self.ow.weather_manager()
        locator = Nominatim(user_agent="bot")

        if city == None:
            city = "Gdańsk"
        else:
            city = city

        country = ", PL"
        loc = locator.geocode(city + country)
        self.lat = loc.latitude
        self.lon = loc.longitude
        self.fore = self.mgr.one_call(lat=self.lat, lon=self.lon)

    def temp(self) -> str:
        temp = (
            self.fore.forecast_daily[0]
            .temperature("celsius")
            .get("day")
        )
        return str(temp)

    def sun_rise(self) -> str:
        sun_rise = datetime.utcfromtimestamp(
            self.fore.forecast_daily[0].sunrise_time()
        ).strftime("%X")
        return str(sun_rise)
