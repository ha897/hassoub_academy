#تقسيم قائمة الى  3ناصر
# r = [1,2,3,4,5,6,7,8,9,7,8,9]
# r2 = []
# for i in range(len(r)//3):
#     r2.append(r[i:i+3])

# print(r2)

r = [1,2,3,4,5,6,7,8,9,7,8,6]
r2 = []
for i in range(0,len(r),3):
    r2.append(r[i:i+3])

print(r2)