a = int(input())
b = map(int, input().split())

lst = list(b)
def printPrimes(lst):
    pres = []
    for i in lst:
        count = 1
        for j in range(2, i+1):
            if i % j == 0:
                count +=1
        if count == 2:
            pres.append(i)
    return pres

pr = printPrimes(lst)

for i in pr:
    if i == pr[-1]:
        print(i)
    else:
        print(i, end=' ')
        
