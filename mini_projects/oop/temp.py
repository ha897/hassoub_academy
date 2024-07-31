temps = [("Damascus", 29), ("Cairo", 36), ("Baghdad", 44), ("Riyadh", 48), ("Beirut", 34), ("Tunis", 30)]

# Fahrenheit
def temp_f(c):
    f = 1.8*c[1] + 32
    return c[0],f

# kelvin
def temp_k(c):
    k = c[1] + 273.15
    return c[0],k
print(list(map(temp_f,temps)))
print(list(map(temp_k,temps)))

# lambda function
print(list(map(lambda c:(c[0],1.8*c[1] + 32),temps)))
print(list(map(lambda c:(c[0],c[1] + 273.15),temps)))

#نمط البرمجة الاجرائية
temp_f2 = []
for i in temps:
    f = 1.8*i[1] + 32
    temp_f2.append((i[0],f))
print(temp_f2)

temp_k2 = []
for i in temps:
    k = i[1] + 273.15
    temp_k2.append((i[0],k))
print(temp_k2)