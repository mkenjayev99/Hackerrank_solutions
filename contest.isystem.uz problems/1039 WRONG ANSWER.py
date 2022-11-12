n = int(input())

for i in range(1, n+1):
    for j in range(i, n+i):
        if j >= 10:
            print(j%10, end=' ')
        else:
            print(j, end=' ')
    print()