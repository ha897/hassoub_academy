#OOP
class Product():
    def __init__(self, id, name, price, count):
        self.id = id
        self.name = name
        self.price = price
        self.count = count
    def discount(self,ratio):
        self.price = self.price - self.price * ratio
    def info(self):
        return f'id: {self.id}, Name: {self.name}, Price: {self.price}$, Count: {self.count}'

iphone_13 = Product(id = 1, name='iPhone 13', price=999, count=10)

samsung_s21 = Product(id=2, name='Samsung Galaxy S20', price=985, count=8)

print(iphone_13.price)

iphone_13.discount(0.1)
print(iphone_13.price)


print(iphone_13.info())
