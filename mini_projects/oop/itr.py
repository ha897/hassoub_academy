def even_num(n):
    for i in range(0,n + 1,2):
        yield i
even = list(even_num(10))
print(even)

def odd_num(n):
    for i in range(1,n + 1,2):
        yield i
odd = list(odd_num(10))
print(odd)

n = 19
even_num = [i for i in range(0,n + 1,2)]
odd_num = [i for i in range(1,n + 1,2)]

print(even_num)
print(odd_num)


