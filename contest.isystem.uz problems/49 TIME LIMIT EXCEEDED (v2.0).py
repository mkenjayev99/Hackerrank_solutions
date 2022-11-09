# SOLVED WITHOUT FUNCTION
a, b, c, d = map(int, input().split())
x = a**b - c
# shundan: EKUB ?
smaller = x if x < d else d
for i in range(1, smaller+1):
    if x % i == 0 and d % i == 0:
        gcd = i
print(gcd)