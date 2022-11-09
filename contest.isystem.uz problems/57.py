n = int(input())
coll = []
c = 0
for i in range(1, n+1):
    c += i
    coll.append(c)

print(sum(coll))