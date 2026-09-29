import requests

URL = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"

response = requests.get(URL, timeout=30)
print("Status code:", response.status_code)

data = response.json()
gempa = data["Infogempa"]["gempa"]

print("Keys:", list(gempa.keys()))
print("Waktu (UTC):", gempa["DateTime"])
print("Magnitude:", gempa["Magnitude"], type(gempa["Magnitude"]))
print("Wilayah:", gempa["Wilayah"])

# contoh parsing kasar
lat, lon = gempa["Coordinates"].split(",")
print("Lat:", float(lat), "| Lon:", float(lon))
print("Magnitude (float):", float(gempa["Magnitude"]))
print("Kedalaman (km):", int(gempa["Kedalaman"].replace(" km", "")))