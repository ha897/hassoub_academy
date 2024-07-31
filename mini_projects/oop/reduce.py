from functools import reduce
#sum
numbers = [1, 2, 3, 4, 5, 6]

def add(x, y):
    return x + y

print(reduce(add, numbers))
"""
1,2,3,4,5,6
3,3,4,5,6
6,4,5,6
10,5,6
15,6
21
"""
#max
numbers = [1, 2, 3, 4, 5, 6]

def max(x, y):
    if y > x:
        return y
    return x
print(reduce(max, numbers))
