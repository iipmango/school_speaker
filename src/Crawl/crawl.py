from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import json
import time
import dbcon

menu_date = []
menu = []
crawl_time = time.time

def crawl():
    context = ssl._create_unverified_context()

    html = urlopen("https://www.kumoh.ac.kr/ko/restaurant01.do", context = context)

    bsObject = BeautifulSoup(html, "html.parser")
    
    link = []
    
    link = bsObject.find_all('tr')
    for text in link[0]:
        menu_date.append(text.text.strip())
    for text in link[1]:
        menu.append(text.text.strip())

    dbcon.dbInsert(json.dumps(menu_date, ensure_ascii = False), json.dumps(menu, ensure_ascii = False))
            
crawl()
