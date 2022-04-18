from datetime import datetime
import os

import requests
from dotenv import load_dotenv
import geocoder

load_dotenv()


class Weather:
    def __init__(self, city=''):
        self.city = city

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return 1.8 * (kelvin - 273.15) + 32

    def get_city_by_coordinates(self):
        try:
            geo_req = geocoder.ip('me')
        except requests.exceptions.ConnectionError:
            return exit("Can't connect to the internet")

        self.city = geo_req.city

    def get_weather_data(self):
        if self.city == '':
            self.get_city_by_coordinates()

        BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
        api_key = os.getenv("WEATHER_API_KEY")
        final_url = BASE_URL + 'appid=' + api_key + '&q=' + self.city

        try:
            response = requests.get(final_url).json()
        except requests.exceptions.ConnectionError:
            return exit("Can't connect to the internet")

        if 'name' not in response:
            return {'city': 'City not found'}

        data = {
            'city': response['name'],
            'sunrise': datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']
                                                 ).strftime('%H:%M:%S'),
            'sunsets': datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']
                                                 ).strftime('%H:%M:%S'),
            'temperature_celsius': {
                'temperature': round(self.kelvin_to_celsius(response['main']['temp']), 2),
                'max_temperature': round(self.kelvin_to_celsius(response['main']['temp_max']), 2),
                'min_temperature': round(self.kelvin_to_celsius(response['main']['temp_min']), 2),
                'feels_like': round(self.kelvin_to_celsius(response['main']['feels_like']), 2),
            },
            'temperature_fahrenheit': {
                'temperature': round(self.kelvin_to_fahrenheit(response['main']['temp']), 2),
                'max_temperature': round(self.kelvin_to_fahrenheit(response['main']['temp_max']), 2),
                'min_temperature': round(self.kelvin_to_fahrenheit(response['main']['temp_min']), 2),
                'feels_like': round(self.kelvin_to_fahrenheit(response['main']['feels_like']), 2),
            },
            'sky': {
                'view': response['weather'][0]['main'],
                'description': response['weather'][0]['description']
            },
            'wind': round(response['wind']['speed'], 2),
            'icon': response['weather'][0]['icon']
        }

        return data
