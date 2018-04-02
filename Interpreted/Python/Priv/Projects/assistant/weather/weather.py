#! /usr/local/bin/python3

import os
import requests as req


class Weather():

    def __init__(self, city):
        self.api_key = os.getenv('WUNDERGROUND_API', '')
        self.brief_dict = dict()
        self.city = city

    def print_weather(self):
        for x in self.brief_dict:
            print(x + ':\t' + self.brief_dict[x])

    def brief(self):
        url = 'http://api.wunderground.com/api/{}/conditions/q/Poland/{}.json'.format(self.api_key, self.city)
        forecast = req.get(url).json()
        self.brief_dict['Weather'] = forecast['current_observation']['weather']
        self.brief_dict['Pressure'] = forecast['current_observation']['pressure_mb'] + 'hPa'
        self.brief_dict['Temperature'] = forecast['current_observation']['UV'] + '°C'
        self.brief_dict['Feels like'] = forecast['current_observation']['feelslike_c'] + '°C'
        self.brief_dict['Humidity'] = forecast['current_observation']['relative_humidity']
        self.print_weather()

    def hour(self):
        url = 'http://api.wunderground.com/api/{}/hourly/q/Poland/{}.json'.format(self.api_key, self.city)
        return req.get(url).json()

    def day(self):
        url = 'http://api.wunderground.com/api/{}/forecast/q/Poland/{}.json'.format(self.api_key, self.city)
        return req.get(url).json()

    def week(self):
        url = 'http://api.wunderground.com/api/{}/forecast10day/q/Poland/{}.json'.format(self.api_key, self.city)
        return req.get(url).json()
