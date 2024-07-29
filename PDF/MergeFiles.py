import os, re, PyPDF2
from pathlib import Path
"""
يجمع ملفات البي دي اف مع حذف الصفحة الاولى لكل ملف
"""
if not os.path.exists("main_folder"):
    os.mkdir("main_folder")
# مجلد الملفات
path_dir = Path(".") / Path("main_folder")
#كل الملفات
files = os.listdir(path_dir)
#نضع بها الملفات المطلوبة
filee = []
#تصفية المجلدات اافتها filee
for filename in files:
    we = re.findall('academy_\d.pdf',filename)
    if we != []:
        filee.append(*we)
#ترتيب 1 2 3
filee.sort()

#فتح ملف الكتابة
fileEnd = open(str(path_dir/Path('artice.pdf')),'wb')
fileWrite = PyPDF2.PdfFileWriter()


for FileName in filee:
    #فتح ملف القرائة
    filePDF = open(str(path_dir/Path(FileName)),'rb')
    fileRead = PyPDF2.PdfFileReader(filePDF)

    #فتح الصفحات من ثاني صفحة للاخير
    for page in range(1,fileRead.numPages):
        Page = fileRead.getPage(page)
        fileWrite.addPage(Page)
    fileWrite.write(fileEnd)
    filePDF.close()

fileEnd.close()