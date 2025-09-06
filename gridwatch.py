import requests
import feedparser
import os
import re

nf="\033[38;2;217;70;239m" #neon_fuchsia
vc="\033[38;2;140;100;220m" #violet_crush
inp="\033[38;2;255;32;121m" #infrared_pink
inb="\033[38;2;126;14;255m" #indigo_blue
cyan="\033[38;2;0;255;255m" #cyan
reset="\033[0m"

hindu_dict={
        1:"https://www.thehindu.com/news/national/feeder/default.rss",
        2:"https://www.thehindu.com/news/international/feeder/default.rss",
        3:"https://www.thehindu.com/sci-tech/science/feeder/default.rss",
        4:"https://www.thehindu.com/business/Industry/feeder/default.rss"
    }
hindu_label={
    1:"INDIA",
    2:"WORLD",
    3:"SCIENCE",
    4:"INDUSTRY"
}
toi_dict={
    1:"https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    2:"https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    3:"https://timesofindia.indiatimes.com/rssfeeds/296589292.cms",
    4:"https://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms",
    5:"https://timesofindia.indiatimes.com/rssfeeds/2647163.cms",
    6:"https://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
    7:"https://timesofindia.indiatimes.com/rssfeeds/4719148.cms",
    8:"https://timesofindia.indiatimes.com/rssfeeds/1898055.cms",
    9:"https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms",
    10:"https://timesofindia.indiatimes.com/rssfeeds/7098551.cms"
}
toi_label={
    1:"TOP STORIES",
    2:"INDIA",
    3:"WORLD",
    4:"SCIENCE",
    5:"ENVIRONMENT",
    6:"TECHNOLOGY",
    7:"SPORTS",
    8:"BUSINESS",
    9:"ENTERTAINMENT",
    10:"NRI"
}
nyt_dict={
    1:"https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    2:"https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml"
}
nyt_label={
    1:"WORLD",
    2:"ASIAPACIFIC"
}

def strip_html(html):
    return re.sub('<[^<]+?>', '', html)

def cprint(color,text,end="\n"):
    print(color+text+reset,end=end)

def clear_screen():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def datafeed(datafeed_name,datafeed_dict,datafeed_label):
    while True:
        clear_screen()
        cprint(nf,f"[ DATAFEED {datafeed_name} ]\n")
        cprint(nf,">> SELECT INTEL CHANNEL\n")
        c=0
        for key in datafeed_label:
            c+=1
            formatted_key = str(key).zfill(2)
            cprint(inp,f"[{formatted_key}] {datafeed_label[key]}")
        cprint(inp,f"[{str(c+1).zfill(2)}] EXIT \n")
        try:
            choice=int(input(f"{nf}>> ENTER : "))
        except:
            continue
        if choice == c+1:
            break
        if choice in datafeed_dict:
            clear_screen()
            datafeed=feedparser.parse(datafeed_dict[choice])
            cprint(nf,f"[ DATAFEED {datafeed_name} ]\n")
            for entry in datafeed.entries:
                cprint(cyan,entry.title)
                formatted_desc=strip_html(entry.description)
                if formatted_desc != "":
                    cprint(inp,formatted_desc+"\n")
                else:
                    print("\n")
        cprint(nf,"\n>> EXIT POINT IDENTIFIED\n>> Press ENTER to exit")
        ch=input("")
    

datafeeds={
    1: lambda: datafeed("HINDU",hindu_dict,hindu_label),
    2: lambda: datafeed("TIMES_OF_INDIA",toi_dict,toi_label),
    3: lambda: datafeed("NY_TIMES",nyt_dict,nyt_label)
}

def source_choice():
    while True:
        clear_screen()
        cprint(nf,"[ GRIDWATCH ACTIVE ]")
        cprint(nf,">> SELECT DATAFEED\n")
        cprint(inp,"[01] HINDU \n[02] TIMES OF INDIA \n[03] NEW YORK TIMES \n[04] EXIT \n")
        try:
            choice=int(input(f"{nf}>> ENTER : "))
        except:
            continue
        if choice == 4:
            clear_screen()
            print(reset)
            return
        if choice in datafeeds:
            datafeeds[choice]()
        else:
            continue

if __name__=='__main__':
    source_choice()