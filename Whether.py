import requests
import os
import geocoder
from string import Template

class Whether():
    def __init__(self):
        self.api_key = os.environ.get("WHETHER_API_KEY")
        self.location = geocoder.ip('me')
        print(self.location)
    def get_current_whether(self):
        url = Template("https://api.openweathermap.org/data/2.5/weather?lat=$lat&lon=$lon&appid=$api_key")
        try:
            response = requests.request("GET", url.substitute(lat=self.location.lat,lon=self.location.lng,api_key=self.api_key))
            response = response.json()
            print(response)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        


if __name__ == "__main__":
    whether = Whether()
    whether.get_current_whether()
    