n = int(input())
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)

for i in lst:
    if i == 1:
        print(1)
    else:
        print(i//2 + 1)