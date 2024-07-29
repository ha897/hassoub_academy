from pdf2docx import Converter
"""
pdf >> word
"""
word_file = 'academy_2.docx'
pdf_file = 'academy_2.pdf'

cv = Converter(pdf_file)
cv.convert(word_file)
# #يحول من الصفحة 3 الى النهاية
# cv.convert(word_file, start = 2)
# #يحول من الصفحة 3 الى 4
# cv.convert(word_file, start = 2, end=4)
cv.close()
