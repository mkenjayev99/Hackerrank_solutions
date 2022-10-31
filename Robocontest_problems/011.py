n = int(input())

arr = map(int, input().split())
lst = list(arr)

max_num = max(lst)
lst.remove(max_num)
max_num = max(lst)

print(sorted(lst))
print(max_num)

