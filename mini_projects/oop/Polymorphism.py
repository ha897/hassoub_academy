class location():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __add__(self,adds):
        return location(self.x + adds, self.y + adds)
    def __str__(self):
        return f"{self.x},{self.y}"


e = location(2,3)
print(e)
print(e+12)