import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# === Configuration ===
API_KEY = '1f06f28e150a8a6d7cef2d41b58dc1b6'  # <-- Replace this with your API key
CITY = 'mumbai'                 # You can change this to any city
UNITS = 'metric'              # Use 'imperial' for Fahrenheit

# === API Request ===
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}'
response = requests.get(URL)

# === Handle API Response ===
if response.status_code != 200:
    print("Failed to get data. Check your API key or city name.")
    exit()

data = response.json()

# === Extract Data ===
temperatures = []
timestamps = []

for item in data['list']:
    temp = item['main']['temp']
    time = item['dt_txt']
    temperatures.append(temp)
    timestamps.append(datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S'))

# === Plotting ===
sns.set(style="darkgrid")  # Optional: sets nice background style
plt.figure(figsize=(12, 6))
plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='teal')

plt.title(f'5-Day Temperature Forecast for {CITY}', fontsize=16)
plt.xlabel('Date and Time', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# === Save and Show ===
plt.savefig('weather_forecast.png')  # Saves the graph as an image file
plt.show()