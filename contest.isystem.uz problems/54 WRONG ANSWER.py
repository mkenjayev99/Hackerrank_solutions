n = map(int, input().split())
lst = list(n)

counted = {i:lst.count(i) for i in lst}

for i, j in sorted(counted.items()):
    print(f"{i}: {'*'*j}")