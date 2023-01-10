'''Class for ineraction with openwhetherapi'''
import os
from string import Template

import geocoder
import requests
import utils
# TODO: create custom error class for messaging
# TODO: split url into pieces and white its in settings and api
# BUG oops something happaned


class WhetherApi():
    """
    Whether class
    """

    def __init__(self):
        self.__api_key = os.environ.get("WHETHER_API_KEY")
        self.location = geocoder.ip('me')

    def get_current_wheather(self):
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
    def get_description_of_current_wheather(self):
        '''generate description of current wheather'''
        wheather_info = self.get_current_wheather()

        temp = utils.number_to_words(wheather_info['current_temperature'])
        wind = utils.number_to_words(wheather_info['current_wind'])
        desc = wheather_info['weather_description']

        full_description = f"""
            Today's whether is {desc}.
            The Temparature is {temp} degrees Celsius.
            The Wind is {wind} meters per second.
        """
        return full_description

if __name__ == "__main__":
    whether = WhetherApi()
    whether.get_current_whether()
