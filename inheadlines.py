import requests
from bs4 import BeautifulSoup
import pyfiglet
import os

scarlet_red="\033[38;2;255;0;60m"
reset="\033[0m"
glitch_violet="\033[38;2;139;0;255m"
dream_blue="\033[38;2;57;163;250m"
lime_green="\033[38;2;175;255;51m"

url_list=["https://www.ndtv.com/india#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/india-global#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/asia#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/europe#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/australia#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/americas#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/africa#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/us#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/uk#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/middle-east#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/science#pfrom=home-ndtv_mainnavigation","https://www.ndtv.com/world/diaspora#pfrom=home-ndtv_mainnavigation"]

def banner():
    print(scarlet_red+pyfiglet.figlet_format("Intel",font="ansi_shadow")+reset,end="\n")

def intel(url):
    banner()
    r = requests.get(url)
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
            print("Website HTML Changed")
    else:
        print("Failed to fetch page. Status code:", r.status_code)
    print(f"{lime_green}EXIT POINT IDENTIFIED\nPress ENTER to exit{reset}")
    ch=input("")
    

def clear_screen():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def choice():
    banner()
    print(f"{lime_green}Select your intel feed, citizen...\n{reset}")
    print(f"{lime_green}1. INDIA\n2.  INDIA GLOBAL\n3.  ASIA\n4.  EUROPE\n5.  AUSTRALIA\n6.  AMERICAS\n7.  AFRICA\n8.  US\n9.  UK\n10. MIDDLE EAST\n11. SCIENCE\n12. DIASPORA\n13. EXIT\n{reset}")
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
    if(ch==13): #Exit
        print(reset)
        clear_screen()
    else:
        clear_screen()
        choice()

if __name__=='__main__':
    clear_screen()
    choice()