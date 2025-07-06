import requests
from bs4 import BeautifulSoup
import pyfiglet
import os

# Colors
scarlet_red=sr="\033[38;2;255;0;60m"
reset="\033[0m"
lime_green=lg="\033[38;2;175;255;51m"
laser_blue=lb="\033[38;2;0;153;255m"
neon_yellow=ny="\033[38;2;255;255;0m"

#url = domain + url_list[x] + suffix
domain="https://www.ndtv.com/"
url_list=["india","world/india-global","world/asia","world/europe","world/australia","world/americas","world/africa","world/us","world/uk","world/middle-east","science","world/diaspora","environment#pfrom=home-nav","auto/car-news","auto/bike-news"]
suffix="#pfrom=home-ndtv_mainnavigation"

def banner():
    print(scarlet_red+pyfiglet.figlet_format("Intel",font="ansi_shadow")+reset,end="\n")

# For Nations, Science, Diaspora and Vehicles
def intel(url):
    banner()
    r = requests.get(domain+url+suffix)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        elements1 = soup.find_all("a", class_="NwsLstPg_ttl-lnk")  
        elements2 = soup.find_all("p",class_="NwsLstPg_txt txt_tct txt_tct-three")
        if elements1 and elements2:
            counter=0
            for a_tag,p_tag in zip(elements1,elements2):  
                counter+=1
                if counter<10:
                    c="[0"+str(counter)+"]"
                else:
                    c="["+str(counter)+"]"
                if a_tag:
                    headline=a_tag.get_text(strip=True)
                if p_tag:
                    titlest=p_tag.get_text(strip=True)
                print(f"{scarlet_red+c+" "+neon_yellow+headline+reset}\n{laser_blue+titlest+reset}\n")
        else:
            print(f"{scarlet_red}Webframe compromised — DOM mutation detected{reset}")
    else:
        print(f"{scarlet_red}>> ERROR. STATUS CODE: ", r.status_code,reset)
    print(f"{scarlet_red}EXIT POINT IDENTIFIED\nPress ENTER to exit{reset}")
    ch=input("")

def environment(url):
    banner()
    r=requests.get(domain+url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        elements = soup.find_all("a", class_="NwsLstPg_ttl-lnk")
        if elements:
            counter=0
            for a_tag in elements:
                counter+=1
                if counter<10:
                    c="[0"+str(counter)+"]"
                else:
                    c="["+str(counter)+"]"
                if a_tag:
                    headline=a_tag.get_text(strip=True)
                    print(f"{scarlet_red+c} {laser_blue+headline}\n{reset}")
        else:
            print(f"{scarlet_red}Webframe compromised — DOM mutation detected{reset}")
    else:
        print(f"{scarlet_red}>> ERROR. STATUS CODE: ", r.status_code,reset)
    print(f"{scarlet_red}EXIT POINT IDENTIFIED\nPress ENTER to exit{reset}")
    ch=input("")

def indian_cities():
    banner()
    city=input(f"{scarlet_red}>> INITIATE TRACE… Enter city name: {laser_blue}").lower()+"-news"
    clear_screen()
    banner()
    url=domain+city+suffix
    r=requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        elements = soup.find_all("a", class_="NwsLstPg_ttl-lnk")
        if elements:
            counter=0
            for a_tag in elements:
                counter+=1
                if counter<10:
                    c="[0"+str(counter)+"]"
                else:
                    c="["+str(counter)+"]"
                if a_tag:
                    headline=a_tag.get_text(strip=True)
                    print(f"{scarlet_red+c} {laser_blue+headline}\n{reset}")
        else:
            print(f"{scarlet_red}Webframe compromised — DOM mutation detected{reset}")
    else:
        if r.status_code == 404:
            print(f"{scarlet_red}[ERROR_404] NO INTEL FOUND FOR SPECIFIED CITY...")
        else:
            print(f"{scarlet_red}>> ERROR. STATUS CODE: ", r.status_code,reset)
    print(f"{scarlet_red}EXIT POINT IDENTIFIED\nPress ENTER to exit{reset}")
    ch=input("")
    

def clear_screen():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def choice():
    while True:
        clear_screen()
        banner()
        print(f"{lb}Select your intel feed, citizen...\n{reset}")
        print(f"{sr}[01]{lb} INDIA\n{sr}[02]{lb} INDIA GLOBAL\n{sr}[03]{lb} ASIA\n{sr}[04]{lb} EUROPE\n{sr}[05]{lb} AUSTRALIA\n{sr}[06]{lb} AMERICAS\n{sr}[07]{lb} AFRICA\n{sr}[08]{lb} US\n{sr}[09]{lb} UK\n{sr}[10]{lb} MIDDLE EAST\n{sr}[11]{lb} SCIENCE\n{sr}[12]{lb} DIASPORA\n{sr}[13]{lb} ENVIRONMENT\n{sr}[14]{lb} INDIAN CITIES\n{sr}[15]{lb} VEHICLE INTEL: CARS\n{sr}[16]{lb} VEHICLE INTEL: BIKES\n{sr}[17]{lb} EXIT\n{reset}")
        try:
            ch=int(input(f"{lb}ENTER: "))
        except:
            clear_screen()
            continue
        print(reset)
        try:
            if(ch==1): #India
                clear_screen()
                intel(url_list[0])
            elif(ch==2): #India Global
                clear_screen()
                intel(url_list[1])
            elif(ch==3): #Asia
                clear_screen()
                intel(url_list[2])
            elif(ch==4): #Europe
                clear_screen()
                intel(url_list[3])
            elif(ch==5): #Australia
                clear_screen()
                intel(url_list[4])
            elif(ch==6): #Americas
                clear_screen()
                intel(url_list[5])
            elif(ch==7): #Africa
                clear_screen()
                intel(url_list[6])
            elif(ch==8): #US
                clear_screen()
                intel(url_list[7])
            elif(ch==9): #UK
                clear_screen()
                intel(url_list[8])
            elif(ch==10): #Middle East
                clear_screen()
                intel(url_list[9])
            elif(ch==11): #Science
                clear_screen()
                intel(url_list[10])
            elif(ch==12): #Diaspora
                clear_screen()
                intel(url_list[11])
            elif(ch==13): #Environment
                clear_screen()
                environment(url_list[12])
            elif(ch==14): #Indian Cities
                clear_screen()
                indian_cities()
            elif(ch==15): #Vehicle Intel: Cars
                clear_screen()
                intel(url_list[13])
            elif(ch==16): #Vehicle Intel: Bikes
                clear_screen()
                intel(url_list[14])
            elif(ch==17): #Exit
                print(reset)
                clear_screen()
                break
            else:
                clear_screen()
        except:
            clear_screen()

if __name__=='__main__':
    clear_screen()
    choice()