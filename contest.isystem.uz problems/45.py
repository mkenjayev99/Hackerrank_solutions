n = int(input())

arr = map(int, input().split())
arr = list(arr)
c = 0
for i in range(n):
    for j in range(n):
        if abs(arr[i] - arr[j]) == 1:
            c +=1

print(c//2)