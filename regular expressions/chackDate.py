import re
"""
استخراج التاريخ
"""
txt = "2022-12-22"
srs = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})",txt)
year1, month1, day1 = srs.groups()
year = srs.group(1)
month = srs.group(2)
day = srs.group(3)

print("the year is " + year1 + " the month is " + month1 + " the day is " + day1)
print("the year is " + year + " the month is " + month + " the day is " + day)
