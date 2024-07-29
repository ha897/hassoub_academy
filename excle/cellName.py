import openpyxl
"""
انشائ وتعديل محتويات ملف الاكسل من سطر الاوامر
"""
# file name
name = input("Enter file location: ")
try:
    #chack file
    excelFile = openpyxl.load_workbook(name)
    SHname = input('what is the name of sheet? ')
except:
    shoo = input("there are no file like that, do you want to create a new folder(Y/N): ").upper()
    #create new
    if shoo == 'Y':
        excelFile = openpyxl.Workbook(name)
    else:
        exit()
try:
    #add sheet
    sheet = excelFile[SHname]
except:
    print("Sheet not found!")
    exit()
while cuol != "" and val != "":
    cuol = input('enter cell name: ')
    val = input('enter cell value: ')
    sheet[cuol] = val

