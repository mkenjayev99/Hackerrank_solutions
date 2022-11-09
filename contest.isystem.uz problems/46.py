n = int(input())
thing_cost = 10000
if n >= 10:
    total = thing_cost*n - thing_cost*n*0.11
else:
    total = thing_cost*n
print(format(total, '.2f'))