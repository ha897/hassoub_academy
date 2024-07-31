import datetime

class Product:
    def __init__(self, name, price, description) -> None:
        self.name = name
        self.price = price
        self.description = description

        #التحقق من عدم وجود الملف مسبقا
        try:
            file = open("products.txt", "x")
            file.write("%-15s %-10s %-20s %s\n"%("name", "price", "description",'time'))
            file.close()
            read = 1
        except FileExistsError:
            #الملف موجود مسبقا
            pass



        #كتابة البيانات
        file = open("products.txt", "a")
        file.write("%-15s %-10s %-20s %s\n"%(name, price, description, datetime.datetime.now()))
        file.close()
        print(name, price, description)

    #طباعة الاسم
    def __str__(self):
        return self.name



    # المقارنة ب==
    def __eq__(self, value: object) -> bool:
        if self.price == value:
            return True
        else:
            return False

    #المقارنة ب >
    def __gt__(self, value: object) -> bool:
        if self.price > value:
            return True
        else:
            return False

    #المقارنة ب >=
    def __ge__(self, value: object) -> bool:
        if self.price > value or  self.price == value:
            return True
        else:
            return False

     #المقارنة ب <
    def __lt__(self, value: object) -> bool:
        if self.price < value:
            return True
        else:
            return False

     #المقارنة ب <=
    def __le__(self, value: object) -> bool:
        if self.price < value or  self.price == value:
            return True
        else:
            return False

    #عرض كل البيانات
    def show_all(self):
        return f"name : {self.name}\nprice : {self.price}\ndescription : {self.description}"


#انشاء كائن
phone = Product("ipone", 12, "good")


# يعرض كل البيانات للمنتج
print(phone.show_all())
#يقارن بالسعر
print(phone > 1)
print(phone < 13)
print(phone >= 12)
print(phone == 12)


