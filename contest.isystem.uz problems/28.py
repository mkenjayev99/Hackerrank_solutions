n = int(input())
arr = map(int, input().split())
lst = list(arr)
lst.sort()

# c = 0
for i in range(n+1):
    for j in range(n+1):
        try:
            if lst[j] == lst[j+1]:
                lst.pop(j+1)
                lst.pop(j)
        except:
            pass
print(lst[0])