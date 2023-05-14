# TASK 3

# arr = [1, 5, 7, 8, 4, 15, 6, 94, 45]
arr = list(map(int, input().split()))
# Bubble sort
for i in range(len(arr)-1):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
