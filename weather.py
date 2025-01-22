# pylint: disable=missing-module-docstring

import sys
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
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
    return None

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    forecast_data = requests.get(f'{BASE_URI}/data/2.5/forecast?lat={lat}&lon={lon}').json()
    forecast = []
    for entry in forecast_data['list']:
        if '12:00:00' in entry['dt_txt']:
            forecast.append({
                'date': entry['dt_txt'][:10],
                'temp': round(entry['main']['temp'] - 273.15),
                'weather': entry['weather'][0]['main']
            })
            if len(forecast) == 5:
                return forecast
    return None

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    result = weather_forecast(city['lat'], city['lon'])
    for day in result:
        print(f'{day["date"]}: {day["weather"]} ({day["temp"]}°C)')

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
