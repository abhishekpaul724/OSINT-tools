import requests
from bs4 import BeautifulSoup
import pyfiglet
import os

scarlet_red="\033[38;2;255;0;60m"
reset="\033[0m"
cyber_green="\033[38;2;7;242;129m"
glitch_violet="\033[38;2;139;0;255m"
dream_blue="\033[38;2;57;163;250m"

def banner():
    print(scarlet_red+pyfiglet.figlet_format("Intel",font="ansi_shadow")+reset,end="\n")

def india():
    banner()
    r = requests.get("https://www.ndtv.com/india#pfrom=home-ndtv_mainnavigation")
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        elements1 = soup.find_all("a", class_="NwsLstPg_ttl-lnk")  
        elements2 = soup.find_all("p",class_="NwsLstPg_txt txt_tct txt_tct-three")
        if elements1 and elements2:
            for a_tag,p_tag in zip(elements1,elements2):  
                if a_tag:
                    headline=a_tag.get_text(strip=True)
                if p_tag:
                    titlest=p_tag.get_text(strip=True)
                print(f"{cyber_green+headline+reset}\n{glitch_violet+titlest+reset}\n")
        else:
            print("Website HTML Changed")
    else:
        print("Failed to fetch page. Status code:", r.status_code)
    print(f"{dream_blue}EXIT POINT IDENTIFIED\nPress ENTER to exit{reset}")
    ch=input("")
    

def clear_screen():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def choice():
    banner()
    print(f"{dream_blue}Select your intel feed, citizen...\n{reset}")
    print(f"{dream_blue}1. INDIA\n2. EXit\n{reset}")
    ch=int(input(f"{dream_blue}ENtEr: "))
    print(reset)
    if(ch==1):
        clear_screen()
        india()
    if(ch==2):
        clear_screen()
    else:
        clear_screen()
        choice()

if __name__=='__main__':
    clear_screen()
    choice()