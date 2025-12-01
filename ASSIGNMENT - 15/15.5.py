import json
import urllib.request
import urllib.parse
import urllib.error
from socket import timeout
import os


API_KEY = "8b2a9cb9d5b942e2f89bacb87905df62"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Save files in the SAME directory as the .py file
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def save_weather_result(result):
    """
    Save extracted weather details into:
    - results.json (append list)
    - results.txt  (one JSON per line)
    """

    json_filename = os.path.join(CURRENT_DIR, "results.json")
    text_filename = os.path.join(CURRENT_DIR, "results.txt")

    # ======= Save to results.json =======
    try:
        if os.path.exists(json_filename):
            with open(json_filename, "r", encoding="utf-8") as f:
                try:
                    old_data = json.load(f)
                except json.JSONDecodeError:
                    old_data = []
        else:
            old_data = []

        old_data.append(result)

        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(old_data, f, indent=4)

    except Exception as e:
        print("Warning: Could not update JSON file:", e)

    # ======= Save to results.txt =======
    try:
        with open(text_filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(result) + "\n")
    except Exception as e:
        print("Warning: Could not update text file:", e)


def get_weather(city):
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

        if str(data.get("cod")) != "200":
            print("City not found. Please enter a valid city.")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()

        result = {
            "city": city,
            "temp": temp,
            "humidity": humidity,
            "weather": description
        }

        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

        print("\nWeather details as JSON:")
        print(json.dumps(result, indent=4))

        # SAVE TO CURRENT FOLDER
        save_weather_result(result)

    except Exception:
        print("Error: Could not connect to API. Check your API key or network connection.")


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
