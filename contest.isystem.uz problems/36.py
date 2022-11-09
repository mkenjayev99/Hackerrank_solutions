n = int(input())

lst = list(range(1, n+1))
c = 0
for i in lst:
    if n % i == 0:
        c += i

print(c)