# SOLVED WITH FUNCTION

a, b, c, d = map(int, input().split())
x = a**b - c
# shundan: EKUB ?

def show_gcd(x, y):
    if x < y:
        smaller = x
    else:
        smaller = y

    for i in range(1, smaller+1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

print(show_gcd(x, d))