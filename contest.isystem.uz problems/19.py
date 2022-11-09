from math import floor, ceil


a = float(input())
if a*10%10 >= 5:
    print(ceil(a))
else:
    print(floor(a))