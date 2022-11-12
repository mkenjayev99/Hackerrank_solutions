n = int(input())

lst = map(int, input().split())
lst = list(lst)

counted = {i:lst.count(i) for i in lst}

val_lst = list(counted.values())
val_lst = sorted(val_lst)
c = 0
for i in range(len(val_lst)):
    if val_lst[i] > 1:
        c += 1
print(c)