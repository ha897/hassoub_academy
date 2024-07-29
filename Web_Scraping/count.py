import bs4
import requests
"""
يحسب عدد الوسوم بالموقع
"""
#يحسب انواع الابنات باتش تي ام ال
res = requests.get('https://en.wikipedia.org')
BU4soup = bs4.BeautifulSoup(res.text, 'html.parser')

table = BU4soup.find_all("table")
div = BU4soup.find_all("div")
link = BU4soup.find_all("a")
image = BU4soup.find_all("img")
vedio = BU4soup.find_all("vedio")
print("this web has:")
if len(table) != 0:
    print("-",len(table),"table")
if len(div) != 0:
    print("-",len(div),"div")
if len(link) != 0:
    print("-",len(link),"link")
if len(image) != 0:
    print("-",len(image),"image")
if len(vedio) != 0:
    print("-",len(vedio),"vedio") 