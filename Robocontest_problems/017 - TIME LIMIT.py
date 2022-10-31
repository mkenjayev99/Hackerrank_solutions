def summ(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def checkx(n):
    s = summ(n)
    return True if n % (s*s) == 0 else False

def getn(n):
    r, x = 0, 0
    while r < n:
        x += 1
        if checkx(x):
            r += 1
    return x

n = int(input())
print(getn(n))