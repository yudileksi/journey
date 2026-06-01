import requests


def get_weather(city_lat, city_lon):
    params = {
        "latitude": city_lat,
        "longitude": city_lon,
        "current_weather": True
    }

    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params=params,
            timeout=5
        )
        response.raise_for_status()

        data = response.json()
        weather = data.get("current_weather", {})

        temperature = weather.get("temperature", "N/A")
        windspeed = weather.get("windspeed", "N/A")

        print(f"Temperature: {temperature}°C")
        print(f"Wind speed: {windspeed} km/h")

    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)