n, m = map(int, input().split())

lst = list(range(n, m+1))

def printPrimes(lst) -> list:
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

average = sum(pr)/len(pr)


print(f"Average-> {average}")
for i in range(len(pr)//2, len(pr)):
    print(pr[i])