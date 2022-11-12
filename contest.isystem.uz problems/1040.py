n = int(input())
lst = list(range(2, n))

divisors = [1, n]
for i in lst:
    if n % i == 0:
        divisors.append(i)

divisors = sorted(divisors)
for i in divisors:
    if i == divisors[-1]:
        print(i)
    else:
        print(i, end=' ')