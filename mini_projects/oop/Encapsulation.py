#OOP
class Product():
    def __init__(self, id, name, price, count):
        self.id = id
        self.name = name
        self.__price = price
        self.count = count
    def discount(self,ratio):
        self.__price = self.price - self.price * ratio
    def info(self):
        return f'id: {self.id}, Name: {self.name}, Price: {self.__price}$, Count: {self.count}'

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return str(self.__price) + '$'

iphone_13 = Product(id = 1, name='iPhone 13', price=999, count=10)
#لم يتغير
iphone_13.__price =0
print(iphone_13.info())
#النص المشوه
print(iphone_13._Product__price)

#نستخدم الاسم المشوه لنغير القيمة
iphone_13._Product__price =0
print(iphone_13.info())