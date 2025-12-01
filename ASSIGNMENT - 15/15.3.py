import json
import urllib.request
import urllib.parse
import urllib.error
from socket import timeout

API_KEY = "8b2a9cb9d5b942e2f89bacb87905df62"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    """
    Fetch weather details for a city using OpenWeatherMap API.
    Handles errors and displays selected fields in user-friendly format.
    """

    # Build the URL with query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # gives temperature in °C
    }

    url = BASE_URL + "?" + urllib.parse.urlencode(params)

    try:
        # Make HTTP request with timeout
        with urllib.request.urlopen(url, timeout=5) as response:
            raw_data = response.read().decode("utf-8")

        # Parse JSON response
        data = json.loads(raw_data)

        # Check for API-level errors (wrong key, wrong city, etc.)
        if str(data.get("cod")) != "200":
            print("Error: Could not connect to API. Check your API key or network connection.")
            # (optional) you can also print: data.get("message")
            return

        # ---------- TASK 3: Extract specific fields ----------
        temp = data["main"]["temp"]          # temperature in °C
        humidity = data["main"]["humidity"]  # humidity in %
        description = data["weather"][0]["description"]  # text like "clear sky"

        # Capitalize description nicely
        description = description.capitalize()

        # ---------- Display in user-friendly format ----------
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

    except (urllib.error.HTTPError,
            urllib.error.URLError,
            timeout,
            Exception):
        # Friendly error message as given in assignment
        print("Error: Could not connect to API. Check your API key or network connection.")
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
