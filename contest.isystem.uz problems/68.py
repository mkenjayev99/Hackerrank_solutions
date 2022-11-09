n = int(input())
lst = []

for i in range(n-1):
    a = int(input())
    lst.append(a)

for i in range(1, n+1):
    if i not in lst:
        print(i)
