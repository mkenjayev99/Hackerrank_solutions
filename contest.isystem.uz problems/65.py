n = int(input())
nums = map(int, input().split())
arr = list(nums)

j = 0
for i in range(0, len(arr[j:])-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
    j += 1

for i in range(len(arr)):
    print("%d" % arr[i], end=" ")