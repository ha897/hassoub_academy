import csv, tabulate
"""
يقوم هذا الكود باستخراج جداول السي اس في وطباعتها بتنسيق معين
"""
# فتح ملف
file = open('data1.csv')
reader = csv.DictReader(file)
DataFile = list(reader)
#البيانات
data =[]
#العناوين
headers = list(DataFile[0].keys())

#استخراج البيانات
for row in DataFile:
    data.append(list(row.values()))

#انشاء جدول وطباعته
table2 = tabulate.tabulate(data, headers, tablefmt="grid")
print(table2)