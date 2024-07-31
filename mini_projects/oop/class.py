#OOP
class numbers():
    def __init__(self,*n):
        self.num = list(n)
        self.sum = sum(n)
        self.min = min(n)
        self.max = max(n)
        self.avr = sum(n)/len(n)



ee= numbers(1,2,3,4)
print(ee.avr)