n = int(input())

lst = list(range(1, n+1))

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

primes = printPrimes(lst)
plot = []
c, i = 0, 0

while n != 1:
    if n % primes[i] == 0:
        plot.append(primes[i])
        n //= primes[i]
        c += 1
    else:
        i += 1

from collections import Counter
res = Counter(plot)

plot_set = list(set(plot))
present = []

for elem in plot_set:
    if res[elem] == 1 and elem != plot_set[-1]:
        present.append(f"{elem} ")
    elif res[elem] == 1 and elem == plot_set[-1]:
        present.append(f"{elem} ")
    elif res[elem] != 1 and elem != plot_set[-1]:
        present.append(f"{elem}^{res[elem]} ")
    elif res[elem] != 1 and elem == plot_set[-1]:
        present.append(f"{elem}^{res[elem]} ")

present.reverse()

for pres in present:
    if pres == present[-1]:
        print(pres, end='\b')
    else:
        print(pres, end='')