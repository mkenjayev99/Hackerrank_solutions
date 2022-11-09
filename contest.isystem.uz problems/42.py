n = input()
n = list(n)

while len(n) != 1:
    summ = 0
    for i in n:
        summ += int(i)
    n = list(str(summ))

print(n[0])