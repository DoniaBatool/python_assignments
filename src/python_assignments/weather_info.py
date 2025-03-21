import requests
from pprint import pprint

API_KEY="534344142d8a238e60302705feef5def"

city = input("Enter the city:")

base_url="http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city
weather_data=requests.get(base_url).json()
pprint(weather_data)
