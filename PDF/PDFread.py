#يمكنها استخراج النص فقط
import PyPDF2
"""
يستخرج النص من ملف البي دي اف
"""
#rb read binary
file = open('HW4 FALL2023 (2).pdf','rb')
fileRead = PyPDF2.PdfFileReader(file)
#عدد الصفحات
print(fileRead.numPages)
#قرائة الصفحات
# الصفحات كالاندكس 0الصفحة الاولى 1الصفحة الثانية
Fpage = fileRead.getPage(0)
#استخراج النص
#يكتب النص الي بالملف   
print(Fpage.extractText())
#اغلاق البرنامج
file.close()