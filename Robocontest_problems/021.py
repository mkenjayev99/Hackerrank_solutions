def desks(n):
    return n//2 if n % 2 == 0 else (n+1)//2

a, b, c = map(int, input().split())
print( desks(a) + desks(b) + desks(c))
