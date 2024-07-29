import requests, bs4
"""
استخراج وطباعة جزء محدد من صفحة ويب معينة
"""
url = 'https://en.wikipedia.org/wiki/Dog'
data = requests.get(url)

#data.text صفحة الوب كاملة كنص
# 'html.parser' تخبره ليعالج على انه اتش تي ام ال
SelectBS4 = bs4.BeautifulSoup(data.text, 'html.parser')
# تكتب به السلكتور الي تجيبه من الوب
SELtext = SelectBS4.select('#siteSub')
# يطبع المكان المحدد من صفحة الويب
print(SELtext)
#يطبع النص فقط
print(SELtext[0].getText())