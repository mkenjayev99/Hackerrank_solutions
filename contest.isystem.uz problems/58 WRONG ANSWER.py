n = int(input())

lst = map(int, input().split())
lst = list(lst)

counted = {i:lst.count(i) for i in lst}

val_lst = list(counted.values())
val_lst = sorted(val_lst)

for i, j in counted.items():
    if j == val_lst[-1]:
        print(i)