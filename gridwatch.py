import requests
import feedparser
import os

nf="\033[38;2;217;70;239m" #neon_fuchsia
vc="\033[38;2;140;100;220m" #violet_crush
inp="\033[38;2;255;32;121m" #infrared_pink
inb="\033[38;2;126;14;255m" #indigo_blue
cyan="\033[38;2;0;255;255m" #cyan
reset="\033[0m"

def hindu():
    hindu_dict={
        1:"https://www.thehindu.com/news/national/feeder/default.rss",
        2:"https://www.thehindu.com/news/international/feeder/default.rss",
        3:"https://www.thehindu.com/sci-tech/science/feeder/default.rss",
        4:"https://www.thehindu.com/business/Industry/feeder/default.rss"
    }
    while True:
        clear_screen()
        cprint(nf,"[ DATAFEED HINDU ]\n")
        cprint(nf,">> SELECT INTEL CHANNEL\n")
        cprint(inp,"[01] INDIA \n[02] WORLD \n[03] SCIENCE \n[04] INDUSTRY \n[05] EXIT \n")
        try:
            choice=int(input(f"{nf}>> ENTER : "))
        except:
            continue
        if choice == 5:
            break
        if choice in hindu_dict:
            clear_screen()
            datafeed=feedparser.parse(hindu_dict[choice])
            cprint(nf,"[ DATAFEED HINDU ]\n")
            for entry in datafeed.entries:
                cprint(cyan,entry.title)
                if entry.description != "":
                    cprint(inb,entry.description+"\n")
                else:
                    print("\n")
        cprint(nf,"\n>> EXIT POINT IDENTIFIED\n>> Press ENTER to exit")
        ch=input("")
    

datafeeds={
    1:hindu
}

def cprint(color,text,end="\n"):
    print(color+text+reset,end=end)

def source_choice():
    while True:
        clear_screen()
        cprint(inb,"[ GRIDWATCH ACTIVE ]")
        cprint(inb,">> SELECT DATAFEED\n")
        cprint(inp,"[01] HINDU \n[02] EXIT \n")
        try:
            choice=int(input(f"{inb}>> ENTER : "))
        except:
            continue
        if choice == 2:
            clear_screen()
            print(reset)
            return
        if choice in datafeeds:
            datafeeds[choice]()

def clear_screen():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__=='__main__':
    source_choice()