import requests
import os
from datetime import datetime

# Colors
scarlet_red=sr="\033[38;2;255;0;60m"
laser_blue=lb="\033[38;2;0;153;255m"
neon_yellow=ny="\033[38;2;255;255;0m"
reset="\033[0m"

# Operator Location Data
operator_latitude="19.076090"
operator_longitude="72.877426"
operator_location="NEO-MUMBAI"

# API Enpoint Data
url="https://api.open-meteo.com/v1/forecast?"

# Weather Code Dictionary
weather_dict = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    4: "Freezing drizzle",
    6: "Freezing rain",
    7: "Freezing rain showers",
    10: "Ice pellets",
    11: "Hail",
    12: "Thunderstorm with rain",
    13: "Thunderstorm with snow",
    14: "Thunderstorm with hail",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Ice crystals",
    80: "Showers",\
    81: "Slight rain showers",
    85: "Snow showers slight",
    86: "Snow showers heavy",
    90: "Thunderstorm without hail",
    91: "Thunderstorm with light rain",
    92: "Thunderstorm with heavy rain",
    93: "Thunderstorm with light snow",
    94: "Thunderstorm with heavy snow",
    95: "Thunderstorm",
    99: "Thunderstorm with hail"
}
wind_dir = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']

def show_weather(latitude,longitude,location=""):
    # Current Weather
    # URL Parameters
    current_params = {
	"latitude": f"{latitude}",
	"longitude": f"{longitude}",
	"current": ["temperature_2m", "precipitation", "weather_code", "wind_speed_10m", "is_day", "wind_direction_10m", "wind_gusts_10m", "cloud_cover","apparent_temperature","relative_humidity_2m","is_day"]
    }
    #Response
    resp=requests.get(url,params=current_params)
    if resp.status_code==200:
        r=resp.json()
        print(scarlet_red+f"CURRENT PHASE: {laser_blue}{"DAY" if r['current']['is_day'] else "NIGHT"}\n"+reset)
        # location Data
        print(scarlet_red+f"Lat and Long : {laser_blue}{latitude}, {longitude}"+reset)
        if location:
            print(scarlet_red+f"Location : {laser_blue}{location}\n"+reset)
        # Weather Data
        print(scarlet_red+f"Temperature : {laser_blue}{r['current']['temperature_2m']}{r['current_units']['temperature_2m']} Feels like {r['current']["apparent_temperature"]}{r['current_units']['apparent_temperature']}"+reset)
        print(scarlet_red+f"Precipitation : {laser_blue}{r['current']['precipitation']}{r['current_units']['precipitation']}"+reset)
        print(scarlet_red+f"Cloud Cover : {laser_blue}{r['current']['cloud_cover']}{r['current_units']['cloud_cover']}"+reset)
        print(scarlet_red+f"Humidity : {laser_blue}{r['current']['relative_humidity_2m']}{r['current_units']['relative_humidity_2m']}\n"+reset)
        if r['current']['weather_code'] in weather_dict:
            current_weather=weather_dict[r['current']['weather_code']]
            print(scarlet_red+f"WEATHER STATUS: {laser_blue}{current_weather}\n"+reset)
        print(scarlet_red+"WIND STATUS:")
        print(scarlet_red+f"Speed: {laser_blue}{r['current']['wind_speed_10m']}{r['current_units']['wind_speed_10m']}",end=" | ")
        print(scarlet_red+f"Gusts: {laser_blue}{r['current']['wind_gusts_10m']}{r['current_units']['wind_gusts_10m']}",end=" | ")
        print(scarlet_red+f"Direction: {laser_blue}{wind_dir[round(r['current']['wind_direction_10m']/45)]} ({r['current']['wind_direction_10m']}{r['current_units']['wind_direction_10m']})")
    

    print(f"{scarlet_red}\nEXIT POINT IDENTIFIED\nPress ENTER to exit{reset}")
    ch=input("")

def custom_lat_long():
    latitude=input(neon_yellow+"INJECT LATITUDE: "+laser_blue)
    longitude=input(neon_yellow+"\nINJECT LONGITUDE: "+laser_blue)  
    clear_screen()
    show_weather(latitude=latitude,longitude=longitude)

def clear_screen():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def choice():
    while True:
        clear_screen()
        print(laser_blue+"WEATHER SYSTEM ACTIVE. ENTER NUMERIC CODE TO PROCEED.\n"+reset)
        print(f"{ny}[01] {lb}OPERATOR'S STATION"+reset)
        print(f"{ny}[02] {lb}LATITUDE AND LONGITUDE"+reset)
        print(f"{ny}[03] {lb}EXIT"+reset)
        try:
            ch=int(input(f"{lb}ENTER: {neon_yellow}"))
        except:
            clear_screen()
            continue
        try:
            if(ch==1):
                clear_screen()
                show_weather(operator_latitude,operator_longitude,operator_location)
            if(ch==2):
                clear_screen()
                custom_lat_long()
            elif(ch==3):
                print(reset)
                clear_screen()
                break
        except:
            clear_screen()

if __name__=='__main__':
    clear_screen()
    choice()