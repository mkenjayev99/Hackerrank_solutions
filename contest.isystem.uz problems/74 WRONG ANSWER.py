# http://cbasicprogram.blogspot.com/2013/01/number-pattern-44.html 
# check up this link to find out more 


n = int(input())

for i in range(1, n):
    for j in range(i, n):
        print(' ', end='')
    for k in range(1, i*2):
        print(k, end='')
    print()

for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(' ', end='')
    for k in range(1, i*2):
        print(k, end='')
    print()