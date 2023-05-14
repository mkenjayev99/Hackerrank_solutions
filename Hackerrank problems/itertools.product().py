from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

lst = list(product(a, b))
for i in lst:
    if i == lst[-1]:
        print(i)
    else:
        print(i, end=' ')
