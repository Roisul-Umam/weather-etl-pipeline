import requests

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": -6.2,
    "longitude": 106.8,
    "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
    "timezone": "Asia/Jakarta",
    "past_days": 1,
    "forecast_days": 1,
}

response = requests.get(URL, params=params, timeout=30)
print("Status code:", response.status_code)

data = response.json()
print("Keys:", list(data.keys()))
print("Jumlah jam:", len(data["hourly"]["time"]))
print("Jam pertama:", data["hourly"]["time"][0])
print("Suhu pertama:", data["hourly"]["temperature_2m"][0])