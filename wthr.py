import requests
import pyfiglet
import os
from datetime import datetime

# Colors
scarlet_red=sr="\033[38;2;255;0;60m"
dream_blue=db="\033[38;2;2;207;247m"
reset="\033[0m"

# Location Data
latitude="19.076090"
longitude="72.877426"
location="NEO-MUMBAI"

# API Enpoint Data
url="https://api.open-meteo.com/v1/forecast?"
params = {
	"latitude": f"{latitude}",
	"longitude": f"{longitude}",
	"current": ["temperature_2m", "precipitation", "weather_code", "wind_speed_10m", "is_day", "wind_direction_10m"]
}

def show_weather():
    r=requests.get(url,params=params).json()
    print(scarlet_red+f"{datetime.now().strftime('%H:%M')}"+reset,end="\n")
    print(scarlet_red+f"Lat and Long : {dream_blue}{latitude}, {longitude}"+reset,end='\n')
    if location:
        print(scarlet_red+f"Location : {dream_blue}{location}"+reset,end='\n')
    print(scarlet_red+f"Temperature : {dream_blue}{r['current']['temperature_2m']}{r['current_units']['temperature_2m']}"+reset,end='\n')
    

def clear_screen():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__=='__main__':
    clear_screen()
    show_weather()