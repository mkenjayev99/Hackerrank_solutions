from math import floor, ceil
a = int(input())
a_n = a/1000
if a%1000 >= 500:
    res = ceil(a_n)*1000
else:
    res = floor(a_n)*1000

print(res)