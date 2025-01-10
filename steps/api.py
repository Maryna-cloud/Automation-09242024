import requests

def get_weather(city: str = "San Francisco", units: str = "metric"):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&units={units}&apikey=mYHhVoYVT5kRYiNlZeuAATbzxlJAH6TG"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    print(response.json())
    data = response.json()
    unit_label = "F" if units == "imperial" else "C"

    return f"Temperature in {city} is {data["data"]["values"]["temperature"]}{unit_label}"

if __name__ == "__main__":
    print(get_weather("Cupertino", units="imperial"))