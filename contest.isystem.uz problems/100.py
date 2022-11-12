n = map(int, input().split())
n = list(n)

max_num = n[0]
for i in n:
    if i > max_num:
        max_num = i

print(max_num)
