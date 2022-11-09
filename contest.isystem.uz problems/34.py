n = int(input())

c, loop = 0, n
for i in range(n):
    if i + loop == n:
        if i > n//2:
            break
        c +=1
        loop -=1
print(c)