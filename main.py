import requests
import json


API_KEY = '247f510a89505aed0714e010bd2ad268'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
CITIES = ['Minsk', 'London', 'Tokyo', 'Paris', 'Berlin']
print("Start getting weather data: ")

for city in CITIES:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_json = response.json()
        city_name = weather_json.get('name')
        temp_main = weather_json.get('main')
        temperature = temp_main.get('temp')
        weather_desc_list = weather_json.get('weather')
        humidity = temp_main.get('humidity', 'N/A')
        description = weather_desc_list[0].get('description')
        print(f'The weather in {city_name}: {temperature}, {description}, Humidity: {humidity}')

    except requests.exceptions.RequestException as e:
        print(f"Error while requesting the weather for {city}: {e}")
    except KeyError as e:
        print(f"Error while data parsing for {city}: {e}")
    except json.JSONDecodeError:
        print(f"Error: uncorrected JSON-response for {city}. Response: {response.text}")
    except IndexError:
        print(f'Error: List "weather" for {city} is empty or uncorrected.')
print("\n Data weather is ok")
