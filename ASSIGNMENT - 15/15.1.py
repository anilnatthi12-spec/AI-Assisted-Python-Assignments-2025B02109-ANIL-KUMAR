
import requests # type: ignore
import json
from datetime import datetime
API_KEY = "8b2a9cb9d5b942e2f89bacb87905df62"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather details for a city using OpenWeather API.
    Includes error handling, JSON display and file storage.
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        # Raise error if HTTP response is not OK
        response.raise_for_status()

        data = response.json()

        # Extract fields
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"].title()

        # Pretty JSON for Task 1
        print("\n===== FULL API JSON RESPONSE =====")
        print(json.dumps(data, indent=4)) 

        # User-friendly output for Task 3 & 4
        print("\n===== WEATHER REPORT =====")
        print(f"City: {city.title()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_desc}")

        # Append results to results.txt (Task 5)
        entry = {
            "city": city.title(),
            "temperature": temperature,
            "humidity": humidity,
            "weather": weather_desc,
            "time": str(datetime.now())
        }

        with open("results.txt", "a") as file:
            file.write(json.dumps(entry) + "\n")

        return entry   # For test cases

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Check your network.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check internet connection.")
    except requests.exceptions.HTTPError:
        print("Error: Invalid city name or API key.")
    except Exception as e:
        print("Unexpected error:", str(e))

    return None
# ✅ CALL THE FUNCTION HERE
get_weather("Hyderabad")   # ← required!