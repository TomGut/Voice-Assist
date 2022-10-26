import os
from datetime import datetime
from typing import Union

from dotenv import load_dotenv
from geopy import Nominatim
from pyowm import OWM


class WeatherSkill:
    """
    Functionality to provide weather forecasting with usage of OpenWeather API.
    OpenWeather API key keept private - loaded from .env (see .env-example).
    """

    load_dotenv()

    def __init__(self, city=None) -> None:
        self.api_key = os.getenv("OPEN_WEATHER_APIKEY")
        if self.api_key != None:
            self.ow = OWM(self.api_key)
            self.mgr = self.ow.weather_manager()
            locator = Nominatim(user_agent="bot")

            # Possibilty to instantiate with None param.
            if city == None:
                self.city = "Gdańsk"
            else:
                self.city = city

            # Country needed for loc.
            country = ", PL"
            loc = locator.geocode(self.city + country)
            self.lat = loc.latitude
            self.lon = loc.longitude
            self.fore = self.mgr.one_call(lat=self.lat, lon=self.lon)
        else:
            return None

    def temp(self) -> Union[str, None]:
        """
        Provides temp in celsius grade.
        forecats_daily[0] indicates present day.

        Returns:
            str: day midian temp.
        """
        if self.api_key != None:
            temp = (
                self.fore.forecast_daily[0]
                .temperature("celsius")
                .get("day")
            )
            return str(temp)
        else:
            return None

    def sun_rise(self) -> Union[str, None]:
        """
        Provides sun rise hour.
        sun_rise - the [0] index in forecast_daily indicates
        present day.

        Returns:
            str: sun rise hour.
        """
        if self.api_key != None:
            sun_rise = datetime.utcfromtimestamp(
                self.fore.forecast_daily[0].sunrise_time()
            ).strftime("%X")
            return str(sun_rise)
        else:
            return None
