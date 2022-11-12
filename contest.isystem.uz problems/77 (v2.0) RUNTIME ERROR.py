n = int(input())
c = 0
for i in range(n):
    a = map(int, input().split())
    a = list(a)
    c += a[i]
print(c)