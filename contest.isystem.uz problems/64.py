n = int(input())

lst = [1, n]

for i in range(2, n):
    if n % i == 0:
        lst.append(i)
        i += 1
lst = sorted(lst)

for i in lst:
    if i == lst[-1]:
        print(i)
    else:
        print(i, end=' ')