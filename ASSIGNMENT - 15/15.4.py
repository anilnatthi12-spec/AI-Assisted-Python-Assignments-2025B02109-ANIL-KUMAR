import json
import urllib.request
import urllib.parse
import urllib.error
from socket import timeout

API_KEY = "8b2a9cb9d5b942e2f89bacb87905df62"   # <-- put your working key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather details for a city using OpenWeatherMap API.
    Uses the city as a function parameter.
    Handles errors for invalid city, network issues, and wrong API key.
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    url = BASE_URL + "?" + urllib.parse.urlencode(params)

    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            raw_data = response.read().decode("utf-8")

        data = json.loads(raw_data)

        # --- INVALID CITY ERROR ---
        if str(data.get("cod")) != "200":
            print("Error: Invalid city. Please enter a valid city name.")
            return

        # --- Extract required fields ---
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()

        # --- Display output ---
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

    except Exception:
        print("Error: Could not connect to API. Check your API key or network connection.")


# -------- MAIN EXECUTION ----------
city_name = input("Enter city name: ")
get_weather(city_name)
