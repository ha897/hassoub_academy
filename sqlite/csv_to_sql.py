import sqlite3, csv
"""
تحويل ملف سي اس في الى قاعدة بيانات
"""
#اتصال بالملف
file = sqlite3.connect('file1.db')
#كائن يسهل الحفض
curs = file.cursor()

fileCsv = open('name2.csv','r')
reader = tuple(csv.reader(fileCsv))

header = str(tuple(reader[0]))
#اضافة العنوان
curs.execute(f'CREATE TABLE if not exists employees {header}')
#اضافة البيانات
for i in reader[1:]:
    curs.execute(f'INSERT INTO employees VALUES {tuple(i)}')
    # print(tuple(i))
file.commit()
file.close()
fileCsv.close()