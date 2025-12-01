import json
import urllib.request
import urllib.parse
import urllib.error
from socket import timeout

# Replace this with your own API key
API_KEY = "8b2a9cb9d5b942e2f89bacb87905df62"   # <-- put your key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Fetch weather details for a city using OpenWeatherMap API.
    Displays JSON output and handles common errors.
    """

    # Build the URL with query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    url = BASE_URL + "?" + urllib.parse.urlencode(params)

    try:
        # Make HTTP request with timeout
        with urllib.request.urlopen(url, timeout=5) as response:
            raw_data = response.read().decode("utf-8")

        # Parse JSON response
        data = json.loads(raw_data)

        # Check for API-level errors (wrong API key, wrong city, etc.)
        # OpenWeatherMap puts 'cod' != 200 when there is an error
        if str(data.get("cod")) != "200":
            # You can also print data.get("message") if you want
            print("Error from API:", data.get("message", "Unknown error"))
            return

        # Pretty print full JSON weather details
        print("Weather data for:", city)
        print(json.dumps(data, indent=4))

    except (urllib.error.HTTPError,
            urllib.error.URLError,
            timeout,
            Exception):
        # Single friendly message for assignment requirement
        print("Error: Could not connect to API. Check your API key or network connection.")


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
