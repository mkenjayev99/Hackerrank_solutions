# 1, 2, 3, 4, 5 < - array | arr

arr = map(int, input().split())
lst = list(arr)

lst.sort()
c = 0
for i in lst:
    c += i
    
max_sum = c - lst[0]
min_sum = c - lst[4]
print(f"{min_sum} {max_sum}")
