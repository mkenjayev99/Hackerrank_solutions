a, b, c, d = map(int, input().split())
x = a**b - c
smaller = x if x < d else d
i = 1
while True:
    if x % i == 0 and d % i == 0:
        gcd = i
    if i == smaller:
        break
    i +=1
print(gcd)