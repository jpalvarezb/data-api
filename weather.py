# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    # Fetch city data from API
    data = requests.get(f'{BASE_URI}/geo/1.0/direct?q={query}&limit=5').json()

    if not data:
        print(f'OpenWeather doesn\'t know about {query.capitalize()}.')
        return None
    if len(data) == 1:
        return data[0]
    if len(data) > 1:
        print(f'More than one {query.capitalize()} found:')
        for i, city in enumerate(data):
            print(f'{i+1}: {city["name"]}')
        idx = int(input('Pick a number for the one you meant.\n>'))
        return data[idx-1]


def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''


def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    weather_forecast(city['lat'], city['lon'])
    # TODO: Display weather forecast for a given city
    pass  # YOUR CODE HERE

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
