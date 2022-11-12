n = int(input())
c = 0
while n!= 0:
    if n %10 == 8:
        c +=1
    n //=10

print(c)