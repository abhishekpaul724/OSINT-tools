import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ndtv.com/india#pfrom=home-ndtv_mainnavigation")

if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    elements = soup.find_all("div", class_="crd_lnk")  
    if elements:
        for elem in elements:
            a_tag = elem.find("a")  
            if a_tag and a_tag.text:
                print(a_tag.get_text(strip=True))
#wsLstPg_txt txt_tct txt_tct-three ptags
    else:
        print("No elements found with class 'crd_lnk'")
else:
    print("Failed to fetch page. Status code:", r.status_code)
