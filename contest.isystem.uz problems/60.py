a = input()
a = list(a)
a = [int(i) for i in a]
summ = sum(a)

res = "NO"
c=0    
for i in range(1, summ+1):
    if summ % i == 0:
       c +=1
if c == 2:
    res = "YES"

print(res)