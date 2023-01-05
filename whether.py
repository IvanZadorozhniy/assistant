'''Class for ineraction with openwhetherapi'''
import os
from string import Template

import geocoder
import requests

# TODO: create custom error class for messaging
# TODO: split url into pieces and white its in settings and api
# BUG oops something happaned


class Whether():
    """
    Whether class
    """

    def __init__(self):
        self.__api_key = os.environ.get("WHETHER_API_KEY")
        self.location = geocoder.ip('me')

    def get_current_whether(self):
        """
        get_current_whether
        Get current state of current weather .
        """
        url_string_template = (
            "https://api.openweathermap.org"
            "/data/2.5/weather"
            "?lat=$lat&lon=$lon&appid=$api_key&units=metric"
        )
        url = Template(url_string_template)
        response = requests.request(
            method="GET",
            url=url.substitute(
                lat=self.location.lat,
                lon=self.location.lng,
                api_key=self.__api_key
            ),
            timeout=10
        )
        response = response.json()

        info = {
            "weather_description": response['weather'][0]['description'],
            "current_temperature": int(float(response['main']['temp'])),
            "current_wind": int(float(response['wind']['speed'])),
        }
        return info


if __name__ == "__main__":
    whether = Whether()
    whether.get_current_whether()
