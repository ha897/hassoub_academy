import openpyxl
"""
انشاء شكل بالاكسل
"""
excelFile = openpyxl.load_workbook('new.xlsx')
sheet = excelFile['firstsheet']

# Charts
title = openpyxl.chart.Reference(sheet, min_col=1, max_col=1, min_row=1, max_row=6)
data = openpyxl.chart.Reference(sheet, min_col=2, max_col=3, min_row=2, max_row=6)
chart = openpyxl. chart.BarChart()
#اسم الرسم
chart.title = 'My Chart'
chart.add_data(data=data)
chart.set_categories(title)

#وضع الرسم E8
sheet.add_chart(chart, 'E8')

excelFile.save(filename = 'new.xlsx')

