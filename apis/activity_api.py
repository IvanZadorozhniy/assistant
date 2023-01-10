'''Module represent the ActivityApi class that help works with boredapi.com'''
import requests

URL = "https://www.boredapi.com/"


class ActivityApi:
    '''Class help work with boredapi.com'''

    def get_some_activity(self):
        '''Get random activity'''

        request = "api/activity"
        response = requests.get(f"{URL}{request}", timeout=5)
        response = response.json()
        return response['activity']
