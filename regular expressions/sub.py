import re
"""
تقطيع الجملة حسب الصيغة
"""
txt = "استبدال-وتقطيع-النصوص-عبر-دوال-الوحدة"
src = re.sub("-"," ",txt)
print(src)
print(src[::-1])