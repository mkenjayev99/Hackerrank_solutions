n = int(input())
c = 0
while n != 0:
    c += n%10
    n //= 10
print(c)