import csv, re, os, pathlib
"""
يقوم بالبحث عن ملفات سي اس في ذات اسم بصيغ محددة ويزيل الترويسة ويجمعها بملف واحد 
"""
# يزيل الترويسة ويجمع محتويات الملفات
def main():
    # المجلد الرئيسي
    main_folder = "csv_folder"
    # اذا لم يكن هناك اي مجلد انشاه
    if not os.path.exists(main_folder):
        os.mkdir(main_folder)
        
    # اسماء الملفات بذاك الامتداد
    listFiles = os.listdir(pathlib.Path(".")/pathlib.Path(main_folder))

    #ملفات csv
    files = []

    #تحقق من الملفات
    for file in listFiles:
        isFilere = re.findall(r'employees_\d.csv',file)
        if isFilere == []:
            continue
        files.append(*isFilere)

    #اضافة القيم لملف جديد
    for Nfile in files:
        values = ReadFile(pathlib.Path(main_folder)/pathlib.Path(Nfile))

        WriteFile(pathlib.Path(main_folder)/pathlib.Path("employees_sum.csv"),values)


#قرائة من ملف
def ReadFile(name):
    file1 = open(name)
    read = csv.reader(file1)
    next(read)
    return list(read)

#كتابة بالملف
def WriteFile(name,values):
    file1 = open(name,'a', newline='')
    write = csv.writer(file1)
    write.writerows(values)
main()