import requests


class ActivityApi:
    
    def get_some_activity(self):
        response = requests.get("https://www.boredapi.com/api/activity", timeout=5)
        response = response.json()
        return response['activity']