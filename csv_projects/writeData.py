"""الكتابة باستخدام الصفوف"""
import csv
# ملف csvعادي
file = open('name1.csv','w',newline='')
writer=csv.writer(file)
#العنوان
header = ["Name","Salary","Date"]
# البيانات
data = [['Hadi','1000','04/08/2021'],
        ['Sara','800','06/04/2021'],
        ['Reem','400','25/02/2020'],
        ['Yara','750','09/07/2020'],
        ['Anas','1200','15/04/2019'],
        ['mahammed','3000','04/08/2021']]
# اضافة العنوان بالمالف
writer.writerow(header)
# اضافة البيانات بالملف
writer.writerows(data)

# _____________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________

"""الكتابة باستخدام قاموس"""
import csv
# باستخدام القاموس
file1 = open('name2.csv','w',newline='')
# العناوين
header1 = ["Name","Salary","Date"]
#البيانات
data1 = [{header1[0]:'Hadi',
            header1[1]:'1000',
            header1[2]:'04/08/2021'},

        {header1[0]:'Sara',
            header1[1]:'800',
            header1[2]:'06/04/2021'},

        {header1[0]:'Reem',
            header1[1]:'400'
            ,header1[2]:'25/02/2020'},

        {header1[0]:'Yara',
            header1[1]:'750',
            header1[2]:'09/07/2020'},

        {header1[0]:'Anas',
            header1[1]:'1200',
            header1[2]:'15/04/2019'},

        {header1[0]:'mahammed',
            header1[1]:'3000',
            header1[2]:'04/08/2021'}]

dictWriter=csv.DictWriter(file1, header1)
#العناوين ينكتب اول
dictWriter.writeheader()
# كتابة المعلومات بالملف
dictWriter.writerows(data1)