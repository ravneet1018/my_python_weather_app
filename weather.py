from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
def get_current_weather(city="Christchurch"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("\n Get current weather conditions \n")
    city = input("\n Please enter a city name:")
    if not bool(city.strip()) :
        city = "Kansas city"
    weather_data = get_current_weather(city)
    pprint(weather_data)
    