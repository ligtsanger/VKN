import requests
import json
from bs4 import BeautifulSoup

def findhref(url):
    hrefs = []
    r = requests.get(url)
    if r.status_code==200:
        wbs = BeautifulSoup(r.text, "html.parser")
        for i in wbs.find_all("a"):
            hrefs.append(i)
    refdict = {url:len(hrefs)}
    json_refdict = json.dumps(refdict, indent=2)
    with open("D:\\git\\VKN\\hrefs.json", "a") as file:
        file.write(json_refdict)
for i in range(5):
   site = input("Введіть посилання веб-сторінки для пошуку гіперпосилань ")
   findhref(site)