import requests
import os
from datetime import datetime

# Colors
nf="\033[38;2;217;70;239m" #neon_fuchsia
vc="\033[38;2;140;100;220m" #violet_crush
inp="\033[38;2;255;32;121m" #infrared_pink
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
        print(f"{inp}>> WX FEED <<\n{reset}")
        print(inp+f"PHS : {nf}{"DAY" if r['current']['is_day'] else "NIGHT"}\n"+reset)
        # location Data
        print(inp+f"LAT : {nf}{latitude} | {inp}LNG : {nf}{longitude}"+reset)
        if location:
            print(inp+f"LOC : {nf}{location}\n"+reset)
        # Weather Data
        print(inp+f"TEMP : {nf}{r['current']['temperature_2m']}{r['current_units']['temperature_2m']} | {inp}FEELS : {nf}{r['current']["apparent_temperature"]}{r['current_units']['apparent_temperature']}"+reset)
        print(inp+f"PRECIP : {nf}{r['current']['precipitation']}{r['current_units']['precipitation']}"+reset)
        print(inp+f"CLD-COV : {nf}{r['current']['cloud_cover']}{r['current_units']['cloud_cover']}"+reset)
        print(inp+f"HUMID : {nf}{r['current']['relative_humidity_2m']}{r['current_units']['relative_humidity_2m']}\n"+reset)
        if r['current']['weather_code'] in weather_dict:
            current_weather=weather_dict[r['current']['weather_code']]
            print(inp+f"WX : {nf}{current_weather}\n"+reset)
        print(inp+"WIND ➤")
        print(inp+f"SPD: {nf}{r['current']['wind_speed_10m']}{r['current_units']['wind_speed_10m']}",end=" | ")
        print(inp+f"GUSTS: {nf}{r['current']['wind_gusts_10m']}{r['current_units']['wind_gusts_10m']}")
        print(inp+f"DIR: {nf}{wind_dir[round(r['current']['wind_direction_10m']/45)]} ({r['current']['wind_direction_10m']}{r['current_units']['wind_direction_10m']})")
    

    print(f"{inp}\n>> EXIT POINT IDENTIFIED\n>> Press ENTER to exit{reset}")
    ch=input("")

def custom_lat_long():
    latitude=input(nf+"INJECT LATITUDE: "+inp)
    longitude=input(nf+"\nINJECT LONGITUDE: "+inp)  
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
        print(vc+"\n>> WEATHER SYSTEM ACTIVE.\n>> ENTER NUMERIC CODE TO PROCEED.\n"+reset)
        print(f"{nf}[01] {inp}OPERATOR'S STATION"+reset)
        print(f"{nf}[02] {inp}LATITUDE AND LONGITUDE"+reset)
        print(f"{nf}[03] {inp}EXIT"+reset)
        try:
            ch=int(input(f"\n{vc}>> ENTER: {nf}"))
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