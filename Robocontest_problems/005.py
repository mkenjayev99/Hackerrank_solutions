# z = 24  , sh.b.: x <= y; x, y, z -> positive integers; x * y = z;
# how much combinations are there?
# ex.:
# x     y        x        y
# 1    24       -1      -24
# 2    12       -2      -12
# 3    8        -3      -8
# 4    6        -4      -6

def howMuchDivisors(z):
    n, c = z, 0
    if z == 0:
        return "-1"
    if z < 0:
        n = -z
    for i in range(1, round(n**(1/2))+1):
        if n % i == 0:
            c += 1
            if i*i != n:
                c += 1
    if c % 2 == 1 and z > 0:
        c += 1
    return c
zed = int(input())    
print(howMuchDivisors(zed))
