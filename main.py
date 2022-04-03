from datetime import datetime
import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather_data(city):
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = os.getenv("WEATHER_API_KEY")
    final_url = BASE_URL + 'appid=' + api_key + '&q=' + city

    response = requests.get(final_url).json()

    data = {
        'city': response['name'],
        'sunrise': datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']
                                             ).strftime('%Y-%m-%d %H:%M:%S'),
        'sunsets': datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']
                                             ).strftime('%Y-%m-%d %H:%M:%S'),
        'temperature_celsius': {
            'temperature': round(kelvin_to_celsius(response['main']['temp']), 2),
            'max_temperature': round(kelvin_to_celsius(response['main']['temp_max']), 2),
            'min_temperature': round(kelvin_to_celsius(response['main']['temp_min']), 2),
            'feels_like': round(kelvin_to_celsius(response['main']['feels_like']), 2),
        },
        'temperature_fahrenheit': {
            'temperature': round(kelvin_to_fahrenheit(response['main']['temp']), 2),
            'max_temperature': round(kelvin_to_fahrenheit(response['main']['temp_max']), 2),
            'min_temperature': round(kelvin_to_fahrenheit(response['main']['temp_min']), 2),
            'feels_like': round(kelvin_to_fahrenheit(response['main']['feels_like']), 2),
        },
        'sky': {
            'view': response['weather'][0]['main'],
            'description': response['weather'][0]['description']
        },
        'wind': round(response['wind']['speed'], 2),
        'icon': response['weather'][0]['icon']
    }

    return data


def get_city_by_coordinates():
    api_key = os.getenv("LOCATION_API_KEY")
    send_url = "http://api.ipstack.com/check?access_key=" + api_key
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)

    return geo_json['city']


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return 1.8 * (kelvin - 273.15) + 32


def main():
    city = get_city_by_coordinates()
    data = get_weather_data(city)
    print(city)
    print(data)


if __name__ == '__main__':
    main()
