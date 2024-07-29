import re
"""
استخراج كل ارقام الهاتف بصيغة 000-000-000
"""
#get all number like \d{3}-\d{3}-\d{4}
def isPhoneNumber(text):

    listNumbers = []
    while True:

        num = re.search(r"\d{3}-\d{3}-\d{4}",text)
        if num == None:
            return listNumbers
        listNumbers.append(num.group())
        text = text.replace(num.group(), "Done")

print(isPhoneNumber("123-123-1223     123-234-4567 23-3-"))

txt = "123-123-1223     123-234-4567 23-3-"
src = re.findall(r"\d{3}-\d{3}-\d{4}",txt)
print(src)