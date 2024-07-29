import csv
"""
انشاء ملف سي اس في والفصل بين البيانات بفاصلة منقوطة بدل الفاصلة العادية
"""
#ملف مفصول ;
file = open('name2.csv','w',newline='')
writer=csv.writer(file,delimiter=';')
writer.writerow(['Name','Salary','Date'])
writer.writerows([['Hadi','1000','04/08/2021'],
                ['Sara','800','06/04/2021'],
                ['Reem','400','25/02/2020'],
                ['Yara','750','09/07/2020'],
                ['Anas','1200','15/04/2019'],
                ['mahammed','3000','04/08/2021']
                ])
