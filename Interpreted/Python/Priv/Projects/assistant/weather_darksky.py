import os
import requests
import json

class WeatherFetcher:

    def __init__(self):
        self.api_key = os.environ['DARKSKY_API_KEY']
        self.latitude = '50.11'
        self.longitude = '19.92'
        self.url = 'https://api.darksky.net/forecast/{}/{},{}?exclude=minutely,daily,flags&units=ca'.format(self.api_key, self.latitude, self.longitude)

    def get_weather(self):
        return json.loads(requests.get(self.url).text)

    def print_weather(self):
        weather = self.get_weather()
        for x in weather['currently']:
            print(weather['currently'][x])
w = WeatherFetcher()
w.print_weather()
