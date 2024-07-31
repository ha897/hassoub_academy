#اخذ صورة تحويلها لبايت
e = open("s.png","rb")
#الملف الي بنحط به الارقام
we  = open("nesser.txt","w")
f = e.read()
lf = list(f)
# كتابة بالملف بالبينري
for i in lf:
    we.write(str(bin(i))+" ")
#وضعها بلست للطباعة
lf2 = [bin(i) for i in lf]
print(lf2)