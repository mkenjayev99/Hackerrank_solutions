collect = ''
n = int(input())
for i in range(n):
    st = input()
    collect += st
collect = list(collect)
c = 0
for j in collect:
    if j == '*':
        c += 1
print(c)