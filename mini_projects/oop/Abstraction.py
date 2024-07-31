from abc import ABC, abstractmethod
#اشكال
class shape(ABC):
    # معناها ان هذا الدااله لازم ان تعرف بكل داله ترث منها
    @abstractmethod
    def area(self):
        pass

#حقول مخصصة لكل اشكال مختلفة

#الشكل المربع
class square(shape):
    def __init__(self, side):
        self.side = side
    #مساحة المربع
    def area(self):
        return self.side ** 2

#الشكل المثلث
class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    #مساحة المثلث
    def area(self):
        return (self.base * self.height) / 2

er = square(3)
print(er.area())