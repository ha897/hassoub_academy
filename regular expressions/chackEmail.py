import re
"""
التحقق من الايميل
"""
def isEmail(text):
    crs = re.search(r"^[A-z1-9]+[\-.]?[A-z1-9]+@\w+.\w{2,3}$",text)
    if crs:
        return True
    return False
email = "hello@gmail.com"
chack = isEmail(email)
if chack:
    print("%s is a valid email adress!"%email)
else:
    print("%s is not a valid email adres!"%email)