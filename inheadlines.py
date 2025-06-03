import requests
from bs4 import BeautifulSoup
import pyfiglet
import os

scarlet_red="\033[38;2;255;0;60m"
reset="\033[0m"
glitch_violet="\033[38;2;139;0;255m"
dream_blue="\033[38;2;2;207;247m"
lime_green="\033[38;2;175;255;51m"

domain="https://www.ndtv.com/"
url_list=["india","india-global","world/asia","world/europe","world/australia","world/americas","world/africa","world/us","world/uk","world/middle-east","science","world/diaspora","environment#pfrom=home-nav"]
suffix="#pfrom=home-ndtv_mainnavigation"

def banner():
    print(scarlet_red+pyfiglet.figlet_format("Intel",font="ansi_shadow")+reset,end="\n")

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
                if a_tag:
                    headline=a_tag.get_text(strip=True)
                if p_tag:
                    titlest=p_tag.get_text(strip=True)
                print(f"{scarlet_red+str(counter)+'.'+lime_green+headline+reset}\n{glitch_violet+titlest+reset}\n")
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
                if a_tag:
                    headline=a_tag.get_text(strip=True)
                    print(f"{scarlet_red+str(counter)}.{dream_blue+headline}\n{reset}")
        else:
            print(f"{scarlet_red}Webframe compromised — DOM mutation detected{reset}")
    else:
        print(f"{scarlet_red}>> ERROR. STATUS CODE: ", r.status_code,reset)
    print(f"{scarlet_red}EXIT POINT IDENTIFIED\nPress ENTER to exit{reset}")
    ch=input("")

def indian_cities():
    banner()
    city=input(f"{scarlet_red}>> INITIATE TRACE… Enter city name: {lime_green}").lower()+"-news"
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
                if a_tag:
                    headline=a_tag.get_text(strip=True)
                    print(f"{scarlet_red+str(counter)}.{dream_blue+headline}\n{reset}")
        else:
            print(f"{scarlet_red}Webframe compromised — DOM mutation detected{reset}")
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
    banner()
    print(f"{lime_green}Select your intel feed, citizen...\n{reset}")
    print(f"{lime_green}1.  INDIA\n2.  INDIA GLOBAL\n3.  ASIA\n4.  EUROPE\n5.  AUSTRALIA\n6.  AMERICAS\n7.  AFRICA\n8.  US\n9.  UK\n10. MIDDLE EAST\n11. SCIENCE\n12. DIASPORA\n13. ENVIRONMENT\n14. INDIAN CITIES\n15. EXIT\n{reset}")
    ch=int(input(f"{lime_green}ENTER: "))
    print(reset)
    if(ch==1): #India
        clear_screen()
        intel(url_list[0])
    if(ch==2): #India Global
        clear_screen()
        intel(url_list[1])
    if(ch==3): #Asia
        clear_screen()
        intel(url_list[2])
    if(ch==4): #Europe
        clear_screen()
        intel(url_list[3])
    if(ch==5): #Australia
        clear_screen()
        intel(url_list[4])
    if(ch==6): #Americas
        clear_screen()
        intel(url_list[5])
    if(ch==7): #Africa
        clear_screen()
        intel(url_list[6])
    if(ch==8): #US
        clear_screen()
        intel(url_list[7])
    if(ch==9): #UK
        clear_screen()
        intel(url_list[8])
    if(ch==10): #Middle East
        clear_screen()
        intel(url_list[9])
    if(ch==11): #Science
        clear_screen()
        intel(url_list[10])
    if(ch==12): #Diaspora
        clear_screen()
        intel(url_list[11])
    if(ch==13): #Environment
        clear_screen()
        environment(url_list[12])
    if(ch==14): #Indian Cities
        clear_screen()
        indian_cities()
    if(ch==15): #Exit
        print(reset)
        clear_screen()
    else:
        clear_screen()
        choice()

if __name__=='__main__':
    clear_screen()
    choice()