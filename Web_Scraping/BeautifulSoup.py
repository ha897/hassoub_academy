import requests, bs4
"""
يحضر رابط صورة من موقع
"""
#ويكا بيديا
url = 'https://ar.wikipedia.org/wiki/%D8%A3%D9%8A_%D9%84%D8%A7%D9%81_%D9%8A%D9%88'
htmlPage = requests.get(url)
#نحول لنوع بيوتفل سوب
htmlPageS = bs4.BeautifulSoup(htmlPage.text, 'html.parser')
#نقططع الجزء الي به الصورة
textF = htmlPageS.select('body > div.vector-header-container > header > div.vector-header-start > a > img')
#محتويات الخلية img
items =textF[0].attrs
#ناخذ الرابط
itemSRC = str(items['src'])
#بويكا بيديا الرابط الرئيسي مع امتداد الصورة يمكننا اخذها واستخدامها بصفحتنا
furl = 'https://ar.wikipedia.org'
#كتابته نصفحة html
print(furl+itemSRC)