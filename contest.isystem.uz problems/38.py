n = input()
for i in range(len(n)//2):
    yes_not = "NO"
    for j in range(len(n)-1-i, len(n)//2-1, -1):
        if n[i] == n[j]:
            yes_not = "YES"
            break
        elif n[i] != n[j]:
            break
print(yes_not)