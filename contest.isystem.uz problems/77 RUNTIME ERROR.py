n = int(input())

arr = []
for i in range(n):
    a = map(int, input().split())
    a = list(a)
    arr.append(a)
    

c = 0
for i in range(n):
    for j in range(n):
        if j == i:
            c += arr[i][j]

print(c)